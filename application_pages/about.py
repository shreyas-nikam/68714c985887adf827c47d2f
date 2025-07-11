
import streamlit as st

def run_about():
    st.title("About Risk Governance Navigator")
    st.markdown("""
    This application is designed to provide an interactive learning and simulation environment for exploring concepts related to risk governance, particularly through the lens of Stafford Beer's Viable System Model (VSM).

    **Viable System Model (VSM)**

    The Viable System Model (VSM) is a cybernetic model developed by Stafford Beer to describe the organizational structure of any viable or autonomous system. A viable system is one that can survive and adapt in a changing environment. The VSM provides a framework for understanding how organizations can be structured and managed to ensure their long-term viability.

    The VSM consists of five interconnected systems:

    *   **System 1: Implementation** - The primary activities of the organization.
    *   **System 2: Coordination** - Ensures the different parts of System 1 work together effectively.
    *   **System 3: Control** - Provides overall direction and control for the organization.
    *   **System 4: Intelligence** - Gathers information about the external environment and provides insights to the organization.
    *   **System 5: Policy** - Sets the overall policies and goals for the organization.

    This application allows you to explore the impact of different VSM components and governance styles on risk mitigation and operational efficiency. By adjusting the parameters and observing the results, you can gain a deeper understanding of how the VSM can be used to improve risk governance in organizations.
    """)
