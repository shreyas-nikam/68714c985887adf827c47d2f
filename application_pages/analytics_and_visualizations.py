import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def run_analytics_and_visualizations():
    st.header("Analytics and Advanced Visualizations")
    st.markdown(r"""
Advanced analytics and visualization capabilities transform raw operational risk data into actionable business intelligence. This comprehensive module combines statistical analysis with interactive visualizations to provide deep insights into cost variability, temporal trends, and categorical risk patterns.

**Integrated Analytics Framework:**  
- **Cost Variability Analysis**: Normalized standard deviation calculations for operational efficiency monitoring
- **Temporal Trend Analysis**: Time-based visualization for pattern identification and anomaly detection
- **Categorical Intelligence**: Segmented analysis for risk profiling and comparative assessment
- **Statistical Modeling**: Mathematical frameworks for quantitative risk measurement

This integrated approach enables organizations to move beyond basic reporting toward predictive analytics and strategic risk intelligence.
""")

    # Cost Variability Analysis Section
    st.subheader("Cost Variability Analysis")
    st.markdown(r"""
**Statistical Methodology:**  
The normalized standard deviation provides a scale-independent measure of cost variability, enabling comparison across different operational contexts and time periods. This metric is essential for monitoring operational efficiency and identifying potential cost control issues.
""")
    
    st.latex(r"""
    \text{Normalized Standard Deviation} = \frac{\sigma_{\text{cost per trade}}}{\text{Max Cost per Trade} - \text{Min Cost per Trade}}
    """)
    
    st.markdown(r"""
Where $\sigma_{\text{cost per trade}}$ represents the standard deviation of cost per trade. Higher normalized standard deviation values indicate greater cost variability, warranting investigation and process improvements.
""")

    def calculate_normalized_std_dev(cost_data):
        if not isinstance(cost_data, list):
            cost_data = list(cost_data)

        if not cost_data:
            raise ValueError("Cost data cannot be empty.")

        if len(cost_data) <= 1:
            return 0.0

        std_dev = np.std(cost_data)
        data_range = max(cost_data) - min(cost_data)

        if data_range == 0:
            return 0.0

        return std_dev / data_range

    df = st.session_state.get('risklab_df', None)

    cost_data_to_use = []
    if df is not None and 'Cost per Trade' in df.columns and not df.empty:
        use_df_data = st.checkbox("Use 'Cost per Trade' from uploaded data", value=True)
        if use_df_data:
            cost_data_to_use = df['Cost per Trade'].tolist()
            st.write(f"Using {len(cost_data_to_use)} data points from 'Cost per Trade' column.")
        else:
            manual_cost_input = st.text_input("Enter comma-separated cost data (e.g., 10, 12, 15, 11, 13)", value="10, 12, 15, 11, 13", help="Enter numeric values separated by commas.")
            try:
                cost_data_to_use = [float(x.strip()) for x in manual_cost_input.split(',') if x.strip()]
            except ValueError:
                st.error("Invalid input. Please enter numeric values separated by commas.")
                cost_data_to_use = []
    else:
        st.info("No valid data loaded yet, please upload a CSV or use the sample data to enable analysis.")
        manual_cost_input = st.text_input("Enter comma-separated cost data (e.g., 10, 12, 15, 11, 13)", value="10, 12, 15, 11, 13", help="Enter numeric values separated by commas.")
        try:
            cost_data_to_use = [float(x.strip()) for x in manual_cost_input.split(',') if x.strip()]
        except ValueError:
            st.error("Invalid input. Please enter numeric values separated by commas.")
            cost_data_to_use = []

    if cost_data_to_use:
        try:
            normalized_std_dev = calculate_normalized_std_dev(cost_data_to_use)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(label="Normalized Std Dev", value=f"{normalized_std_dev:.4f}")
            with col2:
                st.metric(label="Standard Deviation", value=f"{np.std(cost_data_to_use):.2f}")
            with col3:
                st.metric(label="Mean Cost", value=f"{np.mean(cost_data_to_use):.2f}")
                
        except ValueError as e:
            st.error(e)
    else:
        st.warning("No cost data available for calculation.")

    # Add separator
    st.markdown("---")

    # Visualization Section
    st.subheader("Temporal and Categorical Visualizations")

    if df is not None and not df.empty:
        # Time-based Trend Analysis
        st.markdown("**Temporal Trend Analysis:**")
        st.markdown("""
Understanding the evolution of key metrics over time is crucial for identifying patterns, cycles, and anomalies in operational risk. This visualization tracks cost per trade trends, enabling detection of increasing costs, periods of volatility, and operational efficiency changes. Temporal analysis supports predictive modeling and early warning system development for proactive risk management.
""")
        
        try:
            df_sorted = df.sort_values(by='Date')
            fig_trend = px.line(df_sorted, x='Date', y='Cost per Trade',
                                title="Cost per Trade Trend Over Time",
                                labels={"Date": "Date", "Cost per Trade": "Cost per Trade"})
            fig_trend.update_layout(height=400)
            st.plotly_chart(fig_trend, use_container_width=True)
        except Exception as e:
            st.error(f"Error creating time-based trend plot: {e}")

        st.markdown("---")

        # Categorical Analysis
        st.markdown("**Categorical Risk Intelligence:**")
        st.markdown("""
Categorical analysis identifies which operational segments exhibit higher risk profiles or cost inefficiencies by comparing severity levels across different risk categories. This visualization reveals inherent risks associated with specific operational areas, enabling targeted risk management strategies and resource optimization. The segmented approach helps prioritize mitigation efforts and allocate resources to the most critical risk categories.
""")
        
        try:
            avg_severity_by_category = df.groupby('Risk Category')['Severity'].mean().reset_index()
            fig_category = px.bar(avg_severity_by_category, x='Risk Category', y='Severity',
                                   title="Average Severity Across Risk Categories",
                                   labels={"Risk Category": "Risk Category", "Severity": "Average Severity"},
                                   color='Risk Category',
                                   color_discrete_sequence=px.colors.qualitative.Set2)
            fig_category.update_layout(height=400)
            st.plotly_chart(fig_category, use_container_width=True)
        except Exception as e:
            st.error(f"Error creating categorical insights plot: {e}")

