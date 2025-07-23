
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run_risk_profile():
    st.header("Interactive Risk Profile Grid")
    st.markdown(r"""
Risk visualization through likelihood-severity grids transforms complex operational risk data into intuitive, actionable intelligence. This interactive risk profiling tool enables stakeholders to immediately identify, categorize, and prioritize operational risks based on their probability of occurrence and potential business impact. The visual approach facilitates rapid decision-making and resource allocation across diverse risk portfolios.

**Strategic Risk Categorization Framework:**  
The risk profile grid employs a proven four-quadrant classification system that aligns risk assessment with business strategy and resource allocation:

- **Ignore (Low Likelihood, Low Severity)**: Risks with minimal probability and limited impact that typically require no immediate action, allowing focus on higher-priority areas
- **Monitor (High Likelihood, Low Severity)**: Frequent but low-impact risks that warrant ongoing observation and process improvements to prevent accumulation effects
- **Cost (Low Likelihood, High Severity)**: Rare but potentially damaging events requiring contingency planning, insurance coverage, or preventive controls
- **Strategic Risk (High Likelihood, High Severity)**: Critical risks demanding immediate executive attention, comprehensive mitigation strategies, and continuous monitoring

**Operational Application:**  
This grid methodology directly supports regulatory compliance frameworks, strategic planning processes, and day-to-day risk management decisions. By plotting individual risks on the likelihood-severity matrix, organizations can optimize their risk response strategies, ensuring appropriate attention and resources are allocated to the most significant threats to business objectives.
""")

    def plot_risk_profile(severity, likelihood, risk_name):
        fig, ax = plt.subplots(figsize=(4, 3))
        ax.scatter(likelihood, severity, marker='o', s=120, label=risk_name, color='#2ca02c', edgecolor='black', linewidth=1)

        ax.set_xlabel("Likelihood (1-10)", fontsize=9)
        ax.set_ylabel("Severity (1-10)", fontsize=9)
        ax.set_title("Risk Profile", fontsize=10)

        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_xticks(np.arange(0, 11, 1))
        ax.set_yticks(np.arange(0, 11, 1))

        ax.axvline(x=5, color='black', linestyle='--', linewidth=0.8)
        ax.axhline(y=5, color='black', linestyle='--', linewidth=0.8)

        ax.text(2.5, 2.5, "Ignore", fontsize=10, ha='center', va='center', weight='bold', color='gray')
        ax.text(7.5, 2.5, "Monitor", fontsize=10, ha='center', va='center', weight='bold', color='#1f77b4')
        ax.text(2.5, 7.5, "Cost", fontsize=10, ha='center', va='center', weight='bold', color='#ff7f0e')
        ax.text(7.5, 7.5, "Strategic Risk", fontsize=9, ha='center', va='center', weight='bold', color='red')

        ax.legend(fontsize=8, loc='upper left')
        ax.grid(True, linestyle=':', alpha=0.7)
        plt.tight_layout()
        return fig

    # Risk input controls in sidebar
    st.sidebar.subheader("Risk Parameters")
    risk_name_input = st.sidebar.text_input("Risk Name", value="Data Breach", help="Enter a name for the risk to plot.")
    likelihood_input = st.sidebar.slider("Likelihood (1=Low, 10=High)", min_value=1, max_value=10, value=8, help="Likelihood of the risk occurring.")
    severity_input = st.sidebar.slider("Severity (1=Low, 10=High)", min_value=1, max_value=10, value=7, help="Severity of the impact if the risk occurs.")

    # Use columns to control width
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.pyplot(plot_risk_profile(severity=severity_input, likelihood=likelihood_input, risk_name=risk_name_input), use_container_width=True)