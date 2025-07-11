import pytest
from definition_214ddc7d14934e3c9566694cfeba0e7d import perform_comparative_analysis
import matplotlib.pyplot as plt
from unittest.mock import patch

@pytest.fixture
def sample_firm_scores():
    return {"Output": 70, "Process": 80, "Audience": 90, "Success": 85}

@pytest.fixture
def sample_benchmark_scores():
    return {"Output": 60, "Process": 75, "Audience": 80, "Success": 90}

def test_perform_comparative_analysis_valid_input(sample_firm_scores, sample_benchmark_scores):
    # Test that the function runs without errors with valid input dictionaries
    try:
        perform_comparative_analysis(sample_firm_scores, sample_benchmark_scores)
    except Exception as e:
        pytest.fail(f"Function raised an exception: {e}")

def test_perform_comparative_analysis_empty_input():
    # Test that the function handles empty dictionaries gracefully
    try:
        perform_comparative_analysis({}, {})
    except Exception as e:
        pytest.fail(f"Function raised an exception: {e}")

def test_perform_comparative_analysis_missing_keys(sample_firm_scores, sample_benchmark_scores):
    # Test when one of the dictionaries is missing a key
    del sample_firm_scores["Output"]
    with pytest.raises(KeyError): #Expect a KeyError because the code would likely try to access this key
        perform_comparative_analysis(sample_firm_scores, sample_benchmark_scores)

def test_perform_comparative_analysis_invalid_score_type(sample_benchmark_scores):
    #Test when one of the input scores is of the incorrect type
    firm_scores = {"Output": 'high', "Process": 80, "Audience": 90, "Success": 85}
    with pytest.raises(TypeError): #Expect a type error when plotting with string data
        perform_comparative_analysis(firm_scores, sample_benchmark_scores)
