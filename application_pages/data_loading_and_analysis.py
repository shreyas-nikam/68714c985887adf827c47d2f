import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run_data_loading_and_analysis():
    st.header("Data Upload, Validation, and Comparative Analysis")
    st.markdown(r"""
**Data Quality & Validation:**  
The foundation of meaningful operational risk analysis is high-quality, structured data. Poor data quality can lead to misleading risk assessments, incorrect regulatory reporting, and suboptimal business decisions. Here, we systematically load, validate, and summarize trading data across multiple dimensions including:
- **Temporal Analysis**: Date-based trend identification and pattern recognition
- **Cost Metrics**: Trade-level cost analysis for operational efficiency monitoring  
- **Risk Categorization**: Systematic classification of risks by type and severity
- **Data Integrity**: Comprehensive validation of data types, completeness, and consistency

**Comparative Benchmarking:**  
Following data validation, we perform comparative analysis to benchmark your firm's operational risk management quality against industry peers, regulatory standards, or internal targets. This approach provides immediate, actionable insights across four critical quality dimensions that directly impact business performance and regulatory compliance.

**Strategic Integration:**  
This comprehensive approach aligns directly with the 'means of measurement' principle - ensuring that measurement quality drives decision quality. By combining data validation with immediate comparative analysis, organizations can rapidly identify both data quality issues and performance gaps, enabling faster remediation and continuous improvement cycles.

The integrated workflow eliminates common gaps between data preparation and analysis, providing a seamless foundation for all subsequent risk measurement and monitoring activities within the operational risk framework.
""")

    # Data Loading and Validation Section
    st.subheader("Data Upload and Validation")
    
    def load_and_validate_data(uploaded_file=None):
        if uploaded_file is None:
            # Use synthetic data
            data = {
                'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
                'Cost per Trade': [10.5, 12.3, 11.0, 14.8, 9.7],
                'Trade ID': [101, 102, 103, 104, 105],
                'Risk Category': ['Market', 'Operational', 'Credit', 'Market', 'Operational'],
                'Severity': [5, 7, 4, 6, 8],
                'Likelihood': [6, 8, 3, 7, 9],
                'Firm Type': ['A', 'B', 'A', 'B', 'A']
            }
            df = pd.DataFrame(data)
            st.info("Using sample data. Upload a CSV file to use your own data.")
        else:
            try:
                df = pd.read_csv(uploaded_file)
            except Exception as e:
                st.error(f"Error loading file: {e}. Please ensure it's a valid CSV.")
                return None

        required_columns = ['Date', 'Cost per Trade', 'Trade ID', 'Risk Category', 'Severity', 'Likelihood', 'Firm Type']
        for col in required_columns:
            if col not in df.columns:
                st.error(f"Missing required column: `{col}`. Please ensure your CSV has all required columns.")
                return None

        try:
            df['Date'] = pd.to_datetime(df['Date'])
            df['Cost per Trade'] = pd.to_numeric(df['Cost per Trade'])
            df['Trade ID'] = pd.to_numeric(df['Trade ID'], downcast='integer')
            df['Severity'] = pd.to_numeric(df['Severity'], downcast='integer')
            df['Likelihood'] = pd.to_numeric(df['Likelihood'], downcast='integer')
        except Exception:
            st.error("Invalid data type in DataFrame. Please check 'Date', 'Cost per Trade', 'Trade ID', 'Severity', 'Likelihood' columns.")
            return None

        if df[required_columns].isnull().any().any():
            st.warning("Warning: Missing values detected in critical fields. Please review your data.")

        st.subheader("Data Description:")
        # Only describe numeric columns to avoid Arrow serialization issues with datetime
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            st.dataframe(df[numeric_cols].describe())
        else:
            st.write("No numeric columns available for statistical description.")
            
        # st.subheader("Data Types:")
        data_types_df = pd.DataFrame({
            'Column': df.dtypes.index,
            'Data Type': df.dtypes.values.astype(str)
        })
        # st.dataframe(data_types_df)
        st.success("Data loaded and validated successfully.")
        return df

    uploaded_file = st.file_uploader("Upload your CSV data", type=["csv"])
    df = load_and_validate_data(uploaded_file)
    st.session_state['risklab_df'] = df

    # Add a separator
    st.markdown("---")

    # Comparative Analysis Section
    st.subheader("Comparative Analysis: Benchmarking Your Firm")
    st.markdown(r"""
Comparative benchmarking transforms abstract risk management concepts into quantifiable, actionable insights. By evaluating your organization's performance against established benchmarks—industry peers, regulatory standards, or best-practice frameworks—decision makers gain immediate visibility into competitive positioning and improvement opportunities.

**Four-Dimensional Quality Framework:**  
This analysis evaluates operational risk management across four critical dimensions:

- **Output Quality**: Accuracy, completeness, and timeliness of risk reports and deliverables
- **Process Effectiveness**: Efficiency and robustness of internal risk management processes and workflows
- **Audience Satisfaction**: Stakeholder satisfaction with risk management services and communication
- **Success Achievement**: Overall success in achieving strategic risk management objectives

**Methodology:**  
Enter scores on a 0-100 scale for both your firm and your chosen benchmark. The analysis provides gap analysis, performance rankings, and strategic recommendations for enhancing operational risk management maturity.
""")

    def perform_comparative_analysis(firm_scores, benchmark_scores):
        categories = list(firm_scores.keys())
        firm_values = list(firm_scores.values())
        benchmark_values = list(benchmark_scores.values())

        x = np.arange(len(categories))
        width = 0.35

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(x - width/2, firm_values, width, label='Your Firm', color='#1f77b4')
        ax.bar(x + width/2, benchmark_values, width, label='Benchmark', color='#ff7f0e')

        ax.set_xlabel('Quality Areas', fontsize=10)
        ax.set_ylabel('Scores', fontsize=10)
        ax.set_title('Comparative Analysis of Your Firm vs Benchmark', fontsize=14)
        ax.set_xticks(x)
        ax.set_xticklabels(categories, fontsize=10)
        ax.legend(fontsize=10)
        plt.tight_layout()
        return fig


    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Your Firm's Scores (0-100)")
        firm_output = st.number_input("Output", min_value=0, max_value=100, value=75, key='f_out', help="Score for the quality of outputs produced.")
        firm_process = st.number_input("Process", min_value=0, max_value=100, value=80, key='f_proc', help="Score for the effectiveness of internal processes.")
        firm_audience = st.number_input("Audience", min_value=0, max_value=100, value=90, key='f_aud', help="Score for audience satisfaction with risk management.")
        firm_success = st.number_input("Success", min_value=0, max_value=100, value=70, key='f_succ', help="Score for overall success in achieving risk management goals.")
        firm_scores = {'Output': firm_output, 'Process': firm_process, 'Audience': firm_audience, 'Success': firm_success}

    with col2:
        st.markdown("### Benchmark Scores (0-100)")
        bench_output = st.number_input("Output", min_value=0, max_value=100, value=80, key='b_out', help="Score for benchmark's output quality.")
        bench_process = st.number_input("Process", min_value=0, max_value=100, value=75, key='b_proc', help="Score for benchmark's process effectiveness.")
        bench_audience = st.number_input("Audience", min_value=0, max_value=100, value=85, key='b_aud', help="Score for benchmark's audience satisfaction.")
        bench_success = st.number_input("Success", min_value=0, max_value=100, value=75, key='b_succ', help="Score for benchmark's overall success.")
        benchmark_scores = {'Output': bench_output, 'Process': bench_process, 'Audience': bench_audience, 'Success': bench_success}

    # Display the comparative analysis chart
    if st.button("Generate Comparative Analysis", type="primary"):
        fig = perform_comparative_analysis(firm_scores, benchmark_scores)
        st.pyplot(fig, use_container_width=False)
        
