import pytest
from definition_564dc0f0574a4f8db028c39b14df72dc import plot_risk_profile
import matplotlib.pyplot as plt
from unittest.mock import patch

@pytest.fixture(autouse=True)
def close_plots():
    plt.close('all')

@patch('definition_564dc0f0574a4f8db028c39b14df72dc.plt.show')
def test_plot_risk_profile_strategic(mock_show):
    plot_risk_profile(9, 8, "Strategic Risk")
    mock_show.assert_called()

@patch('definition_564dc0f0574a4f8db028c39b14df72dc.plt.show')
def test_plot_risk_profile_ignore(mock_show):
    plot_risk_profile(2, 3, "Ignore Risk")
    mock_show.assert_called()

@patch('definition_564dc0f0574a4f8db028c39b14df72dc.plt.show')
def test_plot_risk_profile_cost(mock_show):
    plot_risk_profile(3, 8, "Cost Risk")
    mock_show.assert_called()
    
@patch('definition_564dc0f0574a4f8db028c39b14df72dc.plt.show')
def test_plot_risk_profile_monitor(mock_show):
    plot_risk_profile(9, 3, "Monitor Risk")
    mock_show.assert_called()

@patch('definition_564dc0f0574a4f8db028c39b14df72dc.plt.show')
def test_plot_risk_profile_edge_case(mock_show):
    plot_risk_profile(5, 5, "Edge Case Risk")
    mock_show.assert_called()
