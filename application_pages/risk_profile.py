
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run_risk_profile():
    st.header("Interactive Risk Profile Grid")
    st.markdown(r"""
**Business Value:**  
Visualizing risks in a grid, plotted by likelihood and severity, provides an intuitive way to categorize and prioritize operational risks. Stakeholders can easily see the most critical risks that require immediate attention. This is directly analogous to the 'Generic Risk Profiles' grid.

The risk profile is split into four sections:
- Ignore
- Monitor
- Cost
- Strategic Risk
""")

    def plot_risk_profile(severity, likelihood, risk_name):
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.scatter(likelihood, severity, marker='o', s=200, label=risk_name, color='#2ca02c', edgecolor='black', linewidth=1)

        ax.set_xlabel("Likelihood (1-10)", fontsize=12)
        ax.set_ylabel("Severity (1-10)", fontsize=12)
        ax.set_title("Risk Profile", fontsize=14)

        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_xticks(np.arange(0, 11, 1))
        ax.set_yticks(np.arange(0, 11, 1))

        ax.axvline(x=5, color='black', linestyle='--', linewidth=0.8)
        ax.axhline(y=5, color='black', linestyle='--', linewidth=0.8)

        ax.text(2.5, 2.5, "Ignore", fontsize=14, ha='center', va='center', weight='bold', color='gray')
        ax.text(7.5, 2.5, "Monitor", fontsize=14, ha='center', va='center', weight='bold', color='#1f77b4')
        ax.text(2.5, 7.5, "Cost", fontsize=14, ha='center', va='center', weight='bold', color='#ff7f0e')
        ax.text(7.5, 7.5, "Strategic Risk", fontsize=14, ha='center', va='center', weight='bold', color='red')

        ax.legend(fontsize=10, loc='upper left')
        ax.grid(True, linestyle=':', alpha=0.7)
        plt.tight_layout()
        return fig

    st.subheader("Visualize a Risk:")
    risk_name_input = st.text_input("Risk Name", value="Data Breach", help="Enter a name for the risk to plot.")
    likelihood_input = st.slider("Likelihood (1=Low, 10=High)", min_value=1, max_value=10, value=8, help="Likelihood of the risk occurring.")
    severity_input = st.slider("Severity (1=Low, 10=High)", min_value=1, max_value=10, value=7, help="Severity of the impact if the risk occurs.")

    st.pyplot(plot_risk_profile(severity=severity_input, likelihood=likelihood_input, risk_name=risk_name_input))