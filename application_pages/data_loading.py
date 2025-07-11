
import streamlit as st
import pandas as pd
import numpy as np

def run_data_loading():
    st.header("Data Upload, Validation, and Summary")
    st.markdown(r"""
**Business Value:**  
The foundation of meaningful operational risk analysis is good-quality, structured data. Here, we load, validate, and summarize the trading data, which is used for all subsequent measurement and analytics. Ensuring correct columns, data types, and identifying potential data quality issues up front prevents spurious metrics and risk management decisions later.

**Technical Details:**  
- Ensures all required columns are present: `Date`, `Cost per Trade`, `Trade ID`, `Risk Category`, `Severity`, `Likelihood`, `Firm Type`
- Checks data types, parses dates, and warns if any columns are missing or data types are incorrect.
- Summarizes data with `.describe()` and displays data types.

This step aligns directly with the 'means of measurement' principle (Handbook, [1])—bad data leads to unreliable measurement, regardless of approach.
""")

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
        st.dataframe(df.describe())
        st.subheader("Data Types:")
        st.dataframe(df.dtypes.astype(str))
        st.success("Data loaded and validated successfully.")
        return df

    uploaded_file = st.file_uploader("Upload your CSV data", type=["csv"])
    df = load_and_validate_data(uploaded_file)
    st.session_state['risklab_df'] = df
    st.sidebar.markdown("---")
