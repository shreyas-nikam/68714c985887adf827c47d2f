import pytest
import pandas as pd
import numpy as np
from definition_fbe6234a321a4a6690d9699d556f6fe8 import calculate_normalized_sd

def create_sample_dataframe(cost_column_values):
    return pd.DataFrame({'Cost_Per_Trade': cost_column_values})

@pytest.mark.parametrize("cost_column_values, expected", [
    ([1, 2, 3, 4, 5], 0.31622776601683794),
    ([10, 10, 10, 10, 10], 0.0),
    ([1, 100], 0.0),
    ([100, 1], 0.0),
    ([1, 2, 3, 4, 100], 0.05012562890050358)
])
def test_calculate_normalized_sd(cost_column_values, expected):
    df = create_sample_dataframe(cost_column_values)
    result = calculate_normalized_sd(df, 'Cost_Per_Trade')
    assert np.isclose(result, expected, rtol=1e-05)

def test_calculate_normalized_sd_empty_dataframe():
    df = pd.DataFrame({'Cost_Per_Trade': []})
    result = calculate_normalized_sd(df, 'Cost_Per_Trade')
    assert np.isnan(result)

def test_calculate_normalized_sd_constant_values():
    df = pd.DataFrame({'Cost_Per_Trade': [5, 5, 5, 5]})
    result = calculate_normalized_sd(df, 'Cost_Per_Trade')
    assert result == 0.0

def test_calculate_normalized_sd_division_by_zero():
    df = pd.DataFrame({'Cost_Per_Trade': [1,1]})
    result = calculate_normalized_sd(df, 'Cost_Per_Trade')
    assert np.isnan(result)
