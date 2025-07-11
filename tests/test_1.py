import pytest
import pandas as pd
from definition_1ba5ee678e3e4d39b4960c4c39bc614e import calculate_vsm_performance

@pytest.fixture
def sample_data():
    data = pd.DataFrame({
        'Risk_Event_Flag': [True, False, True, False, True],
        'Risk_Severity': [5, 2, 8, 1, 4],
        'Operational_Efficiency_Baseline': [0.8, 0.9, 0.7, 0.6, 0.85]
    })
    return data

def test_calculate_vsm_performance_active_governance(sample_data):
    result = calculate_vsm_performance(sample_data, 0.8, 0.7, 0.9, 0.6, 0.5, 0.4, 'Active')
    assert isinstance(result, pd.DataFrame)
    assert 'Risk_Mitigation_Effectiveness' in result.columns
    assert 'Operational_Efficiency' in result.columns

def test_calculate_vsm_performance_reactive_governance(sample_data):
    result = calculate_vsm_performance(sample_data, 0.5, 0.4, 0.6, 0.3, 0.2, 0.1, 'Reactive')
    assert isinstance(result, pd.DataFrame)
    assert 'Risk_Mitigation_Effectiveness' in result.columns
    assert 'Operational_Efficiency' in result.columns

def test_calculate_vsm_performance_preventative_governance(sample_data):
    result = calculate_vsm_performance(sample_data, 0.6, 0.5, 0.7, 0.4, 0.3, 0.2, 'Preventative')
    assert isinstance(result, pd.DataFrame)
    assert 'Risk_Mitigation_Effectiveness' in result.columns
    assert 'Operational_Efficiency' in result.columns

def test_calculate_vsm_performance_empty_data():
    data = pd.DataFrame()
    result = calculate_vsm_performance(data, 0.7, 0.6, 0.8, 0.5, 0.4, 0.3, 'Active')
    assert isinstance(result, pd.DataFrame)

def test_calculate_vsm_performance_invalid_governance(sample_data):
    with pytest.raises(ValueError):
        calculate_vsm_performance(sample_data, 0.7, 0.6, 0.8, 0.5, 0.4, 0.3, 'Invalid')

