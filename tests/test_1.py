import pytest
import pandas as pd
from definition_3d9109a5f95c4553a895fe01d9b4edeb import apply_filters

@pytest.fixture
def sample_dataframe():
    data = {'Date': pd.to_datetime(['2023-01-01', '2023-02-15', '2023-03-20', '2023-04-05', '2023-05-10']),
            'Business_Unit': ['Retail', 'Wholesale', 'Retail', 'Investment', 'Wholesale'],
            'Event_Type': ['Fraud', 'System Failure', 'Process Error', 'Fraud', 'Process Error'],
            'Loss_Amount': [100, 200, 150, 300, 250]}
    return pd.DataFrame(data)

def test_apply_filters_date_range(sample_dataframe):
    df = apply_filters(sample_dataframe, start_date='2023-02-01', end_date='2023-04-01', selected_business_units=[], selected_event_types=[], min_loss_amount=0, max_loss_amount=500)
    assert len(df) == 2
    assert df['Date'].min() >= pd.to_datetime('2023-02-01')
    assert df['Date'].max() <= pd.to_datetime('2023-04-01')

def test_apply_filters_business_unit(sample_dataframe):
    df = apply_filters(sample_dataframe, start_date='2023-01-01', end_date='2023-05-31', selected_business_units=['Retail'], selected_event_types=[], min_loss_amount=0, max_loss_amount=500)
    assert len(df) == 2
    assert all(df['Business_Unit'] == 'Retail')

def test_apply_filters_event_type(sample_dataframe):
    df = apply_filters(sample_dataframe, start_date='2023-01-01', end_date='2023-05-31', selected_business_units=[], selected_event_types=['Fraud'], min_loss_amount=0, max_loss_amount=500)
    assert len(df) == 2
    assert all(df['Event_Type'] == 'Fraud')

def test_apply_filters_loss_amount(sample_dataframe):
    df = apply_filters(sample_dataframe, start_date='2023-01-01', end_date='2023-05-31', selected_business_units=[], selected_event_types=[], min_loss_amount=200, max_loss_amount=300)
    assert len(df) == 3
    assert df['Loss_Amount'].min() >= 200
    assert df['Loss_Amount'].max() <= 300

def test_apply_filters_no_filters(sample_dataframe):
    df = apply_filters(sample_dataframe, start_date=None, end_date=None, selected_business_units=[], selected_event_types=[], min_loss_amount=None, max_loss_amount=None)
    assert len(df) == len(sample_dataframe)
