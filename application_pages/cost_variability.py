
import streamlit as st
import numpy as np
import pandas as pd # Import pandas to access st.session_state['risklab_df']

def run_cost_variability():
    st.header("Normalized Standard Deviation Calculator")
    st.markdown(r"""
**Business Value:**  
The normalized standard deviation of cost per trade is a valuable metric for monitoring operational efficiency and identifying potential cost overruns. By understanding the variability in cost per trade, firms can better control expenses and improve overall profitability. This aligns with the Handbook's discussion of learning from other industries [5].

**Technical Details:**  
- The `calculate_normalized_std_dev` function calculates the normalized standard deviation using the following formula:
""")
    st.latex(r"""
    \text{Normalized Standard Deviation} = \frac{\sigma_{\text{cost per trade}}}{\text{Max Cost per Trade} - \text{Min Cost per Trade}}
""")
    st.markdown(r"""
- Where $\sigma_{\text{cost per trade}}$ is the standard deviation of cost per trade. Normalization helps to compare variability across different scales of cost.
A higher normalized standard deviation indicates greater variability in cost per trade, which may warrant further investigation and process improvements.
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

    st.subheader("Calculate Normalized Standard Deviation:")

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
            st.metric(label="Normalized Standard Deviation", value=f"{normalized_std_dev:.4f}")
        except ValueError as e:
            st.error(e)
    else:
        st.warning("No cost data available for calculation.")
    st.markdown("---")
