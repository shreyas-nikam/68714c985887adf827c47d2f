
import streamlit as st
import pandas as pd
import plotly.express as px

def run_additional_visualizations():
    st.header("Time-based Trend Plot")
    st.markdown("""
**Business Value:**  
Understanding the evolution of key metrics over time is crucial for identifying patterns, cycles, and anomalies in operational risk. This plot visualizes the trend of 'Cost per Trade' over time, allowing for the detection of increasing/decreasing costs or periods of higher volatility.

**Technical Details:**  
- Utilizes the `Date` and `Cost per Trade` columns from the loaded data.
- Presents a line chart to show the temporal trend using Plotly.
""")

    df = st.session_state.get('risklab_df', None)

    if df is not None and not df.empty:
        # Time-based Trend Plot
        st.subheader("Cost per Trade Trend Over Time")
        try:
            df_sorted = df.sort_values(by='Date')
            fig_trend = px.line(df_sorted, x='Date', y='Cost per Trade',
                                title="Trend of Cost per Trade Over Time",
                                labels={"Date": "Date", "Cost per Trade": "Cost per Trade"})
            st.plotly_chart(fig_trend, use_container_width=True)
        except Exception as e:
            st.error(f"Error creating time-based trend plot: {e}")

        st.markdown("---")

        st.header("Categorical Insights")
        st.markdown("""
**Business Value:**  
Categorical analysis helps identify which segments (e.g., risk categories, firm types) exhibit higher or lower risk profiles or cost efficiencies. This visualization provides an aggregated comparison of 'Severity' by 'Risk Category', offering insights into inherent risks associated with different operational areas.

**Technical Details:**  
- Groups the loaded data by 'Risk Category'.
- Calculates the average 'Severity' for each category.
- Presents a bar chart for easy comparison using Plotly.
""")

        st.subheader("Average Severity by Risk Category")
        try:
            avg_severity_by_category = df.groupby('Risk Category')['Severity'].mean().reset_index()
            fig_category = px.bar(avg_severity_by_category, x='Risk Category', y='Severity',
                                   title="Average Severity Across Risk Categories",
                                   labels={"Risk Category": "Risk Category", "Severity": "Average Severity"})
            st.plotly_chart(fig_category, use_container_width=True)
        except Exception as e:
            st.error(f"Error creating categorical insights plot: {e}")

        st.markdown("---")
    else:
        st.info("Upload data to see the Additional Visualizations.")

    st.header("Summary and Next Steps")
    st.markdown("""
In this lab, you have:

- Explored three primary means of measuring operational risk management quality: Standard-Based, Comparative, and Predictive.
- Learned about the importance and challenges of data quality and validation for risk functions.
- Used visual tools to benchmark your organization's effectiveness, plot risk profiles, and monitor operational efficiency with normalized standard deviation.
- Understood, with practical examples, why **audience satisfaction** is often the most feasible and actionable metric.
- Connected operational risk metrics and grids to their strategic interpretations.

**Business Value Summary:**  
These tools provide both immediate value—by helping you benchmark and prioritize risk areas—and longer-term value in building a measurement culture that aligns with both feasibility and best practices (see Handbook references [1-5]).

## Further Reading

For deeper insights, consult the referenced chapters in the 'Operational Risk Manager Handbook', especially the discussion of means of measurement, 'unrealistic' versus 'feasible' approaches, and generic risk profile grids.
""")
