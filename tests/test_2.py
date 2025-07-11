import pytest
from definition_c5a1e8749ebb46e2a9368042b442c162 import plot_loss_trend
import pandas as pd
import matplotlib.pyplot as plt

@pytest.fixture
def sample_dataframe():
    data = {'Date': pd.to_datetime(['2023-01-01', '2023-01-15', '2023-02-01', '2023-02-15', '2023-03-01']),
            'Loss_Amount': [100, 150, 200, 250, 300],
            'Incident_Count': [1, 2, 1, 3, 2]}
    return pd.DataFrame(data)

def test_plot_loss_trend_monthly(sample_dataframe, monkeypatch):
    # Mock plt.show() to avoid displaying the plot during testing
    monkeypatch.setattr(plt, 'show', lambda: None)
    plot_loss_trend(sample_dataframe, 'M')
    # Basic assertion to check if the plot was generated (can be improved with more specific checks)
    assert plt.gcf().number > 0

def test_plot_loss_trend_quarterly(sample_dataframe, monkeypatch):
    monkeypatch.setattr(plt, 'show', lambda: None)
    plot_loss_trend(sample_dataframe, 'Q')
    assert plt.gcf().number > 0

def test_plot_loss_trend_yearly(sample_dataframe, monkeypatch):
    monkeypatch.setattr(plt, 'show', lambda: None)
    plot_loss_trend(sample_dataframe, 'Y')
    assert plt.gcf().number > 0

def test_plot_loss_trend_empty_dataframe(monkeypatch):
    monkeypatch.setattr(plt, 'show', lambda: None)
    empty_df = pd.DataFrame({'Date': [], 'Loss_Amount': [], 'Incident_Count': []})
    plot_loss_trend(empty_df, 'M')
    assert plt.gcf().number > 0 # should not raise error, but produce empty plot
    
def test_plot_loss_trend_invalid_granularity(sample_dataframe, monkeypatch):
    monkeypatch.setattr(plt, 'show', lambda: None)
    with pytest.raises(KeyError):
        plot_loss_trend(sample_dataframe, 'invalid')
