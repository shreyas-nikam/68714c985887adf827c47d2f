import pytest
from definition_29dfc8d5939f4a68a963cb30d28f99b4 import load_and_validate_data
import pandas as pd
import os

@pytest.fixture
def sample_csv_file(tmp_path):
    # Create a temporary CSV file for testing
    file_path = tmp_path / "test_data.csv"
    data = {'Incident_ID': [1, 2, 3],
            'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
            'Loss_Amount': [100, 200, 300],
            'Business_Unit': ['A', 'B', 'A']}
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    return str(file_path)

def test_load_and_validate_data_file_found(sample_csv_file):
    """Test loading data from a valid CSV file."""
    df = load_and_validate_data(file_path=sample_csv_file, generate_sample=False)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert len(df) == 3

def test_load_and_validate_data_file_not_found_generate_sample(tmp_path):
    """Test generating a sample dataset when the file is not found."""
    df = load_and_validate_data(file_path=str(tmp_path / "nonexistent.csv"), generate_sample=True)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

def test_load_and_validate_data_no_file_path_generate_sample():
    """Test generating a sample dataset when no file path is provided."""
    df = load_and_validate_data(file_path=None, generate_sample=True)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

def test_load_and_validate_data_empty_file(tmp_path):
    """Test handling an empty CSV file."""
    file_path = tmp_path / "empty.csv"
    with open(file_path, 'w') as f:
        pass  # Create an empty file

    with pytest.raises(pd.errors.EmptyDataError):
        load_and_validate_data(file_path=str(file_path), generate_sample=False)

def test_load_and_validate_data_invalid_date_format(tmp_path):
    """Test handling invalid date formats in the CSV file."""
    file_path = tmp_path / "invalid_date.csv"
    data = {'Incident_ID': [1], 'Date': ['invalid-date'], 'Loss_Amount': [100], 'Business_Unit': ['A']}
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)

    df_loaded = load_and_validate_data(file_path=str(file_path), generate_sample=False)
    assert isinstance(df_loaded['Date'].iloc[0], pd.Timestamp)
