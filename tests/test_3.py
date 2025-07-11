import pytest
import numpy as np
from definition_621af50fe1094cfdb3ee5e0ed8f66044 import calculate_normalized_std_dev

def test_calculate_normalized_std_dev_typical():
    cost_data = [10, 12, 15, 13, 16]
    expected = np.std(cost_data) / (max(cost_data) - min(cost_data))
    assert calculate_normalized_std_dev(cost_data) == pytest.approx(expected)

def test_calculate_normalized_std_dev_identical_values():
    cost_data = [5, 5, 5, 5, 5]
    assert calculate_normalized_std_dev(cost_data) == 0.0

def test_calculate_normalized_std_dev_empty_list():
    cost_data = []
    with pytest.raises(ZeroDivisionError):
        calculate_normalized_std_dev(cost_data)

def test_calculate_normalized_std_dev_single_value():
    cost_data = [10]
    assert calculate_normalized_std_dev(cost_data) == 0.0

def test_calculate_normalized_std_dev_negative_values():
    cost_data = [-10, -12, -15, -13, -16]
    expected = np.std(cost_data) / (max(cost_data) - min(cost_data))
    assert calculate_normalized_std_dev(cost_data) == pytest.approx(expected)
