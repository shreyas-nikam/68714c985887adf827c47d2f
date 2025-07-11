import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

@st.cache_data
def generate_synthetic_data():
    """Generates synthetic data for risk governance simulation."""
    num_rows = 100
    timestamps = pd.date_range(start='2023-01-01', periods=num_rows, freq='D')
    vsm_system_ids = np.random.randint(1, 11, num_rows)
    risk_event_flags = np.random.choice([0, 1], num_rows, p=[0.8, 0.2])
    risk_severities = np.random.choice(['Low', 'Medium', 'High'], num_rows, p=[0.5, 0.3, 0.2])
    operational_efficiency_baselines = np.random.uniform(0.7, 0.95, num_rows)
    policy_clarity_impacts = np.random.normal(0, 0.1, num_rows)
    intelligence_strength_impacts = np.random.normal(0, 0.15, num_rows)
    coordination_level_impacts = np.random.normal(0, 0.08, num_rows)
    control_effectiveness_impacts = np.random.normal(0, 0.12, num_rows)
    feedforward_strength_impacts = np.random.normal(0, 0.09, num_rows)
    feedback_strength_impacts = np.random.normal(0, 0.11, num_rows)
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

@st.cache_data
def calculate_vsm_performance(data, user_policy_clarity, user_intel_strength, user_coordination_level, user_control_effectiveness, user_feedforward_strength, user_feedback_strength, user_governance_style):
    """Calculates Risk Mitigation Effectiveness and Operational Efficiency based on VSM parameters."""
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input data must be a pandas DataFrame.")
    if user_governance_style not in ['Reactive', 'Preventative', 'Active']:
        raise ValueError("Invalid governance style. Must be 'Reactive', 'Preventative', or 'Active'.")
    processed_data = data.copy()
    severity_map = {'Low': 0.2, 'Medium': 0.5, 'High': 1.0}
    processed_data['Risk_Severity_Numeric'] = processed_data['Risk_Severity'].map(severity_map)
    processed_data['Risk_Mitigation_Effectiveness'] = (
        user_policy_clarity +
        user_intel_strength +
        user_coordination_level +
        user_control_effectiveness +
        user_feedforward_strength +
        user_feedback_strength
    ) / 6
    if user_governance_style == 'Reactive':
        processed_data['Operational_Efficiency'] = processed_data['Operational_Efficiency_Baseline'] * (1 - 0.1 * processed_data['Risk_Severity_Numeric'])
    elif user_governance_style == 'Preventative':
        processed_data['Operational_Efficiency'] = processed_data['Operational_Efficiency_Baseline'] * (1 - 0.05 * processed_data['Risk_Severity_Numeric'])
    else:
        processed_data['Operational_Efficiency'] = processed_data['Operational_Efficiency_Baseline'] * (1 - 0.025 * processed_data['Risk_Severity_Numeric'])
    return processed_data.drop(columns=['Risk_Severity_Numeric'])

def run_simulation():
    st.header("VSM Simulation")
    synthetic_data = generate_synthetic_data()
    st.sidebar.header("VSM Component Strengths")
    user_policy_clarity = st.sidebar.slider("Policy Clarity", 0.0, 1.0, 0.5, help="Clarity of policy guidelines and procedures.")
    user_intel_strength = st.sidebar.slider("Intelligence Strength", 0.0, 1.0, 0.5, help="Strength of intelligence gathering and analysis.")
    user_coordination_level = st.sidebar.slider("Coordination Level", 0.0, 1.0, 0.5, help="Level of coordination between different departments and systems.")
    user_control_effectiveness = st.sidebar.slider("Control Effectiveness", 0.0, 1.0, 0.5, help="Effectiveness of control mechanisms and procedures.")
    user_feedforward_strength = st.sidebar.slider("Feedforward Strength", 0.0, 1.0, 0.5, help="Strength of feedforward mechanisms for anticipating future risks.")
    user_feedback_strength = st.sidebar.slider("Feedback Strength", 0.0, 1.0, 0.5, help="Strength of feedback mechanisms for learning from past events.")
    st.sidebar.header("Governance Style")
    user_governance_style = st.sidebar.selectbox("Select Governance Style", ['Reactive', 'Preventative', 'Active'], help="Choose the governance style to simulate.")
    performance_df = calculate_vsm_performance(
        synthetic_data, user_policy_clarity, user_intel_strength, user_coordination_level,
        user_control_effectiveness, user_feedforward_strength, user_feedback_strength, user_governance_style
    )
    avg_risk_mitigation = performance_df['Risk_Mitigation_Effectiveness'].mean()
    avg_operational_efficiency = performance_df['Operational_Efficiency'].mean()
    st.metric(label="Average Risk Mitigation Effectiveness", value=f"{avg_risk_mitigation:.2f}")
    st.metric(label="Average Operational Efficiency", value=f"{avg_operational_efficiency:.2f}")

    # Time Series Trend Plot
    fig_trend = px.line(
        performance_df, x="Timestamp",
        y=["Operational_Efficiency", "Risk_Mitigation_Effectiveness"],
        title="Performance Trends Over Time"
    )
    fig_trend.update_layout(yaxis_title="Performance Value", font=dict(size=14))
    st.plotly_chart(fig_trend, use_container_width=True)

    # Aggregated Comparison Charts
    avg_oe_by_severity = performance_df.groupby('Risk_Severity')['Operational_Efficiency'].mean().reset_index()
    fig_oe_severity = px.bar(avg_oe_by_severity, x='Risk_Severity', y='Operational_Efficiency', title='Average Operational Efficiency by Risk Severity')
    fig_oe_severity.update_layout(font=dict(size=14))
    st.plotly_chart(fig_oe_severity, use_container_width=True)

    avg_rme_by_severity = performance_df.groupby('Risk_Severity')['Risk_Mitigation_Effectiveness'].mean().reset_index()
    fig_rme_severity = px.bar(avg_rme_by_severity, x='Risk_Severity', y='Risk_Mitigation_Effectiveness', title='Average Risk Mitigation Effectiveness by Risk Severity')
    fig_rme_severity.update_layout(font=dict(size=14))
    st.plotly_chart(fig_rme_severity, use_container_width=True)

    with st.expander("Show Raw Data"):
        st.write(performance_df.head())
