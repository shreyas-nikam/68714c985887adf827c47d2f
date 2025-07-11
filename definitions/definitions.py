import pandas as pd
import numpy as np

def generate_synthetic_data():
    """Generates synthetic data for risk governance simulation."""

    num_rows = 100  # Number of data points

    # Generate data for each column
    timestamps = pd.date_range(start='2023-01-01', periods=num_rows, freq='D')
    vsm_system_ids = np.random.randint(1, 11, num_rows)  # IDs from 1 to 10
    risk_event_flags = np.random.choice([0, 1], num_rows, p=[0.8, 0.2])  # 0 or 1, 20% chance of risk
    risk_severities = np.random.choice(['Low', 'Medium', 'High'], num_rows, p=[0.5, 0.3, 0.2])
    operational_efficiency_baselines = np.random.uniform(0.7, 0.95, num_rows)  # Values between 0.7 and 0.95
    policy_clarity_impacts = np.random.normal(0, 0.1, num_rows)  # Mean 0, std dev 0.1
    intelligence_strength_impacts = np.random.normal(0, 0.15, num_rows)  # Mean 0, std dev 0.15
    coordination_level_impacts = np.random.normal(0, 0.08, num_rows)  # Mean 0, std dev 0.08
    control_effectiveness_impacts = np.random.normal(0, 0.12, num_rows)  # Mean 0, std dev 0.12
    feedforward_strength_impacts = np.random.normal(0, 0.09, num_rows)  # Mean 0, std dev 0.09
    feedback_strength_impacts = np.random.normal(0, 0.11, num_rows)  # Mean 0, std dev 0.11

    # Create the DataFrame
    data = pd.DataFrame({
        'Timestamp': timestamps,
        'VSM_System_ID': vsm_system_ids,
        'Risk_Event_Flag': risk_event_flags,
        'Risk_Severity': risk_severities,
        'Operational_Efficiency_Baseline': operational_efficiency_baselines,
        'Policy_Clarity_Impact': policy_clarity_impacts,
        'Intelligence_Strength_Impact': intelligence_strength_impacts,
        'Coordination_Level_Impact': coordination_level_impacts,
        'Control_Effectiveness_Impact': control_effectiveness_impacts,
        'Feedforward_Strength_Impact': feedforward_strength_impacts,
        'Feedback_Strength_Impact': feedback_strength_impacts
    })

    return data

import pandas as pd

def calculate_vsm_performance(data, user_policy_clarity, user_intel_strength, user_coordination_level, user_control_effectiveness, user_feedforward_strength, user_feedback_strength, user_governance_style):
    """Calculates Risk Mitigation Effectiveness and Operational Efficiency based on VSM parameters."""

    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input data must be a pandas DataFrame.")

    if user_governance_style not in ['Reactive', 'Preventative', 'Active']:
        raise ValueError("Invalid governance style. Must be 'Reactive', 'Preventative', or 'Active'.")

    # Risk Mitigation Effectiveness Calculation
    data['Risk_Mitigation_Effectiveness'] = (
        user_policy_clarity +
        user_intel_strength +
        user_coordination_level +
        user_control_effectiveness +
        user_feedforward_strength +
        user_feedback_strength
    ) / 6

    # Operational Efficiency Calculation
    if user_governance_style == 'Reactive':
        data['Operational_Efficiency'] = data['Operational_Efficiency_Baseline'] * (1 - 0.1 * data['Risk_Severity'])
    elif user_governance_style == 'Preventative':
        data['Operational_Efficiency'] = data['Operational_Efficiency_Baseline'] * (1 - 0.05 * data['Risk_Severity'])
    else:  # Active
        data['Operational_Efficiency'] = data['Operational_Efficiency_Baseline'] * (1 - 0.025 * data['Risk_Severity'])

    return data