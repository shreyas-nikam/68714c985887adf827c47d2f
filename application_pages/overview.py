
import streamlit as st

def run_overview():
    st.title("Risk Governance Navigator")
    st.markdown("""
    Welcome to the **Risk Governance Navigator Lab**!

    ## Business Value

    Modern organizations face complex and evolving risks. To thrive, they must not only respond to risk events but also anticipate and mitigate them proactively. This application introduces the **Viable System Model (VSM)** framework, as explained in the 'Operational Risk Manager Handbook', and demonstrates how it can be leveraged to govern risk effectively.

    The VSM, developed by Stafford Beer, provides a cybernetic view of organizations, emphasizing interconnected functions and information flows. Through interactive simulations, scenario exploration, and key performance indicators, this application enables you to visualize and understand how governance styles affect risk and efficiency.

    ## What You'll Learn

    - Interpret the VSM's seven key organizational elements.
    - Explore the relationships between policy, intelligence, coordination, control, and process in risk governance.
    - Understand and distinguish between **Reactive**, **Preventative**, and **Active** governance structures.
    - Visualize impacts of governance strategy adjustments on risk mitigation and operational performance.

    ---
    ## Measuring Governance Effectiveness: VSM Performance Calculation

    At the core of effective risk governance is the ability to measure how well our systems are performing. This section introduces the calculation of two critical metrics: **Risk Mitigation Effectiveness** and **Operational Efficiency**. These metrics provide a tangible way to understand the impact of different VSM components and chosen governance styles on an organization's ability to manage risk and operate smoothly. By understanding these metrics, organizations can make informed decisions to optimize their governance strategies.

    ### Risk Mitigation Effectiveness

    This metric represents the overall strength of the VSM in mitigating risks. It's calculated as the average of the user-defined effectiveness of various VSM components.
    """)
    st.latex(r"""
        \text{Risk Mitigation Effectiveness} = \frac{\text{Policy Clarity} + \text{Intelligence Strength} + \text{Coordination Level} + \text{Control Effectiveness} + \text{Feedforward Strength} + \text{Feedback Strength}}{6}
    """)
    st.markdown("""
    Where each component strength ranges, for example, from $0$ to $1$, with higher values indicating better performance. This average provides a holistic view of the system's preparedness against risks.

    ### Operational Efficiency

    Operational efficiency reflects how smoothly operations run, considering the impact of risk events and the chosen governance style. Different governance styles (Reactive, Preventative, Active) have varying impacts on efficiency, especially when a risk event occurs.
    """)
    st.latex(r"""
        \text{Operational Efficiency} = \text{Operational Efficiency Baseline} \times (1 - \text{Risk Impact Factor} \times \text{Risk Severity})
    """)
    st.markdown("""
    The `Risk Impact Factor` depends on the `user_governance_style`:
    - **Reactive**: Assumes a higher penalty to efficiency when a risk occurs (e.g., $0.1$ for a 'High' severity risk). This style is characterized by responding *after* a risk has materialized, leading to more significant disruptions.
    - **Preventative**: Assumes a moderate penalty (e.g., $0.05$ for a 'High' severity risk). This style focuses on preventing risks, reducing their impact if they do occur.
    - **Active**: Assumes the lowest penalty (e.g., $0.025$ for a 'High' severity risk). An active governance style continuously monitors and adapts, minimizing the impact of even severe risks.

    The `Risk Severity` values ('Low', 'Medium', 'High') are mapped internally to numerical values to scale their impact on efficiency. This model demonstrates how a proactive governance approach can cushion the blow of operational risks, leading to higher sustained efficiency.
    """)
    # References can be placed at the end of the Streamlit app
    st.markdown("""
    ---
    **References:**
    1.  Chapter 2: Process, Operational Risk Manager Handbook, p. 23
    2.  Chapter 2: Risk Governance & Strategic Planning, Operational Risk Manager Handbook, p. 15
    3.  Chapter 2: Governing and Governance, Operational Risk Manager Handbook, p. 11
    """)
