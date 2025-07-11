id: 68714c985887adf827c47d2f_documentation
summary: Risk Governance Lab 2 Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Risk Governance Navigator: A Streamlit Codelab

## Introduction and Overview
Duration: 0:10:00

Welcome to the Risk Governance Navigator codelab! In this lab, you will explore a Streamlit application designed to simulate and visualize the impact of different governance strategies and Viable System Model (VSM) components on organizational risk mitigation and operational efficiency.

**Why is this important?**

In today's dynamic and complex business environment, organizations face a myriad of potential risks, from operational disruptions to cyberattacks and regulatory non-compliance. Effective risk governance is not just a compliance requirement; it's a strategic imperative for survival and growth. Understanding how organizational structures and processes influence risk management is crucial.

This application provides an interactive sandbox based on the **Viable System Model (VSM)**, a powerful framework introduced by Stafford Beer, for understanding how complex systems (like organizations) can maintain viability and adapt. By simulating different scenarios, you can gain insights into how elements like policy, intelligence, coordination, and control, combined with various governance styles (Reactive, Preventative, Active), directly affect key performance indicators like risk mitigation effectiveness and operational efficiency.

**What concepts will we explore?**

*   **Viable System Model (VSM):** We'll touch upon the core idea of VSM as a cybernetic model for organizational structure and function.
*   **VSM Components in Risk Governance:** How different functions within the VSM (like Policy, Intelligence, Control, etc.) contribute to managing risk.
*   **Governance Styles:** Understanding the distinction and impact of Reactive, Preventative, and Active approaches to risk governance.
*   **Key Performance Indicators (KPIs):** We will focus on two calculated metrics:
    *   **Risk Mitigation Effectiveness:** A measure of the overall strength of the VSM components in place.
    *   **Operational Efficiency:** A measure of how smoothly operations run, particularly under stress from risk events, and how this is influenced by the governance style.

The application calculates these key metrics based on user inputs and a simulated environment. Let's look at the formulas used, as shown in the application's Overview section:

**Risk Mitigation Effectiveness:**

This metric is calculated as the average of the effectiveness scores assigned to various VSM components.

$$
\text{Risk Mitigation Effectiveness} = \frac{\text{Policy Clarity} + \text{Intelligence Strength} + \text{Coordination Level} + \text{Control Effectiveness} + \text{Feedforward Strength} + \text{Feedback Strength}}{6}
$$

Here, each component's strength is a value typically ranging from $0$ to $1$. A higher average indicates a more robust system for mitigating risks.

**Operational Efficiency:**

This metric reflects the impact of risks and governance style on baseline operational efficiency.

$$
\text{Operational Efficiency} = \text{Operational Efficiency Baseline} \times (1 - \text{Risk Impact Factor} \times \text{Risk Severity})
$$

The `Risk Impact Factor` is dependent on the chosen `user_governance_style`:
*   **Reactive:** A higher factor (e.g., $0.1$ for High Severity) leading to a larger drop in efficiency during a risk event.
*   **Preventative:** A moderate factor (e.g., $0.05$ for High Severity), showing reduced impact compared to Reactive.
*   **Active:** The lowest factor (e.g., $0.025$ for High Severity), demonstrating minimal impact from risks due to proactive management.

`Risk Severity` is mapped to numerical values (e.g., Low=0.2, Medium=0.5, High=1.0) to scale its effect. This formula highlights how different governance approaches buffer the organization differently against risk impacts.

By working through this codelab, you will set up, run, and interact with the application, gaining hands-on experience with these concepts and how they can be simulated.

<aside class="positive">
Before proceeding, ensure you have Python installed on your system. This application uses Streamlit, Pandas, NumPy, and Plotly.
</aside>

## Setting up the Environment
Duration: 0:05:00

To run the application, you need to set up your Python environment and install the necessary libraries.

1.  **Create a project directory:**
    Create a folder for your project, for example, `risk_navigator_app`. Inside this folder, create another folder named `application_pages`.

2.  **Save the code:**
    Save the provided code into the following files within your project directory structure:
    *   `risk_navigator_app/app.py`
    *   `risk_navigator_app/application_pages/overview.py`
    *   `risk_navigator_app/application_pages/simulation.py`
    *   `risk_navigator_app/application_pages/about.py`

3.  **Install required libraries:**
    Open your terminal or command prompt, navigate to the `risk_navigator_app` directory, and run the following command to install Streamlit, Pandas, NumPy, and Plotly:

    ```console
    pip install streamlit pandas numpy plotly
    ```

    This command installs all the libraries required for the application to run.

<aside class="positive">
It's a good practice to use a virtual environment (like `venv` or `conda`) to manage dependencies for your Python projects.
</aside>

You are now ready to run the application!

## Exploring the Application Structure and Overview Page
Duration: 0:07:00

Let's start by running the application and exploring its structure.

1.  **Run the application:**
    Open your terminal or command prompt, navigate to the `risk_navigator_app` directory, and run the main application file:

    ```console
    streamlit run app.py
    ```

    This command will start the Streamlit server, and your web browser should automatically open a new tab displaying the application.

    If the browser doesn't open automatically, copy the local URL shown in your terminal (usually `http://localhost:8501`) and paste it into your browser's address bar.

2.  **Observe the structure:**
    The application is a multi-page Streamlit app. You'll see a sidebar on the left with a title ("QuLab"), a logo, a divider, and a "Navigation" selectbox. The main area of the page displays content based on the selection in the sidebar.

    This structure is defined in the `app.py` file:

    ```python
    # app.py
    import streamlit as st

    st.set_page_config(page_title="Risk Governance Navigator", layout="wide")
    st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
    st.sidebar.divider()
    st.title("QuLab")
    st.divider()
    st.markdown("""
    In this lab, we will explore the Risk Governance Lab 2 application. This application is designed to help you understand and visualize the effects of different governance styles and the effectiveness of VSM components on risk mitigation and operational efficiency.
    """)

    # Navigation logic
    page = st.sidebar.selectbox(label="Navigation", options=["Overview", "Simulation", "About"])

    # Display content based on selection
    if page == "Overview":
        from application_pages.overview import run_overview
        run_overview()
    elif page == "Simulation":
        from application_pages.simulation import run_simulation
        run_simulation()
    elif page == "About":
        from application_pages.about import run_about
        run_about()
    ```

    This code sets up the page configuration, adds sidebar elements, and uses an `if/elif/else` block to call functions from different page modules (`overview.py`, `simulation.py`, `about.py`) based on the user's selection in the `st.sidebar.selectbox`.

3.  **Explore the Overview Page:**
    When you first run the app, the "Overview" page is displayed by default. This page is generated by the `run_overview()` function in `application_pages/overview.py`.

    Read through the content on this page:
    *   **Business Value:** Explains the importance of risk governance and introduces the VSM framework.
    *   **What You'll Learn:** Outlines the key takeaways from the lab.
    *   **Measuring Governance Effectiveness:** Details the calculation of the two key metrics: Risk Mitigation Effectiveness and Operational Efficiency, including the mathematical formulas you saw earlier and explanations of how governance style impacts Operational Efficiency.

    <aside class="positive">
    The Overview page provides the foundational theoretical context for the simulation you will explore next. Pay attention to the explanation of the VSM metrics and how governance styles affect efficiency.
    </aside>

This static page serves as an introduction. The real interaction happens on the "Simulation" page.

## Deep Dive into the Simulation Page
Duration: 0:15:00

Navigate to the "Simulation" page by selecting "Simulation" from the "Navigation" selectbox in the sidebar.

This page is powered by the `run_simulation()` function in `application_pages/simulation.py` and allows you to interactively change parameters and see their impact on the calculated metrics and visualizations.

1.  **Sidebar Controls:**
    Look at the sidebar again. Below the navigation, there are two new sections:
    *   **VSM Component Strengths:** Six sliders allowing you to adjust the simulated effectiveness of different VSM components (Policy Clarity, Intelligence Strength, Coordination Level, Control Effectiveness, Feedforward Strength, Feedback Strength). Each slider ranges from $0.0$ to $1.0$.
    *   **Governance Style:** A selectbox to choose between 'Reactive', 'Preventative', and 'Active' governance styles.

    These controls represent the inputs you can provide to the simulation model. Changing these values updates the calculations and visualizations on the main page.

2.  **Main Content Area:**
    The main area displays the results of the simulation:
    *   **Average Metrics:** Two `st.metric` cards showing the `Average Risk Mitigation Effectiveness` and `Average Operational Efficiency` across the simulated time period.
    *   **Performance Trends Over Time:** A line chart showing how Operational Efficiency and Risk Mitigation Effectiveness trend over the simulated timestamps.
    *   **Aggregated Comparison Charts:** Bar charts comparing `Average Operational Efficiency by Risk Severity` and `Average Risk Mitigation Effectiveness by Risk Severity`.

    <aside class="positive">
    Experiment by changing the slider values for VSM components and selecting different governance styles. Observe how the average metrics and the charts update in real-time. For example, try setting all VSM component sliders to 1.0 and compare the results between the 'Reactive' and 'Active' governance styles.
    </aside>

3.  **Interpreting the Visualizations:**
    *   The **Performance Trends Over Time** plot shows fluctuations. The drops in Operational Efficiency correspond to simulated risk events (you can see the `Risk_Event_Flag` and `Risk_Severity` columns if you show the raw data). Risk Mitigation Effectiveness is generally more stable as it's an average of your fixed component strengths, though in a more complex model, it might also fluctuate.
    *   The **Average Operational Efficiency by Risk Severity** bar chart clearly shows the impact of risk severity on efficiency. You should observe a lower average efficiency for 'High' severity risks compared to 'Low' severity risks.
    *   The **Average Risk Mitigation Effectiveness by Risk Severity** bar chart will likely show a relatively flat line across severities, as the RME calculation doesn't inherently depend on individual risk severity *during* simulation; it's based on the *system's capacity* (your slider inputs) to handle risks *in general*. This chart helps reinforce that RME is a property of the system's structure, not a reaction to a specific risk event.

4.  **Show Raw Data:**
    Expand the "Show Raw Data" section at the bottom. This displays the first few rows of the processed DataFrame used to generate the metrics and charts. You can see the original synthetic data columns (`Timestamp`, `Risk_Event_Flag`, `Risk_Severity`, etc.) alongside the calculated `Risk_Mitigation_Effectiveness` and `Operational_Efficiency` columns. This helps you see the underlying data structure.

<aside class="negative">
Remember that the underlying data is *synthetic* and generated randomly each time `generate_synthetic_data` is called (though cached for consistent re-calculation within a session). The goal is to illustrate the *model's behavior* based on VSM concepts and governance styles, not to provide a forecast based on real historical data.
</aside>

The simulation page is the core interactive part of the application, allowing you to model different governance scenarios.

## Understanding the Simulation Code
Duration: 0:20:00

Let's look at the code behind the Simulation page (`application_pages/simulation.py`) to understand how the simulation data is generated and the metrics are calculated.

The `simulation.py` file contains three main parts: data generation, calculation logic, and the Streamlit UI rendering.

```python
# application_pages/simulation.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Data generation function
@st.cache_data
def generate_synthetic_data():
    """Generates synthetic data for risk governance simulation."""
    # ... (code for generating DataFrame)
    return data

# Calculation function
@st.cache_data
def calculate_vsm_performance(data, user_policy_clarity, user_intel_strength, user_coordination_level, user_control_effectiveness, user_feedforward_strength, user_feedback_strength, user_governance_style):
    """Calculates Risk Mitigation Effectiveness and Operational Efficiency based on VSM parameters."""
    # ... (code for validation, mapping, and calculation)
    return processed_data

# Streamlit UI function
def run_simulation():
    # ... (code for UI elements and calling functions)
    pass
```

### Data Generation (`generate_synthetic_data`)

```python
# application_pages/simulation.py (within generate_synthetic_data)
@st.cache_data
def generate_synthetic_data():
    """Generates synthetic data for risk governance simulation."""
    num_rows = 100
    timestamps = pd.date_range(start='2023-01-01', periods=num_rows, freq='D')
    vsm_system_ids = np.random.randint(1, 11, num_rows) # Dummy VSM system IDs
    risk_event_flags = np.random.choice([0, 1], num_rows, p=[0.8, 0.2]) # 20% chance of a risk event
    risk_severities = np.random.choice(['Low', 'Medium', 'High'], num_rows, p=[0.5, 0.3, 0.2]) # Random severities
    operational_efficiency_baselines = np.random.uniform(0.7, 0.95, num_rows) # Baseline efficiency
    # These impacts are not directly used in the current calculation but show potential for expansion
    policy_clarity_impacts = np.random.normal(0, 0.1, num_rows)
    intelligence_strength_impacts = np.random.normal(0, 0.15, num_rows)
    # ... other impact columns
    data = pd.DataFrame({
        # ... define columns
    })
    return data
```

*   This function creates a pandas DataFrame representing 100 days of synthetic data.
*   It includes columns like `Timestamp`, `Risk_Event_Flag` (indicating if a risk occurred on that day), `Risk_Severity`, and a `Operational_Efficiency_Baseline`.
*   Notice the `@st.cache_data` decorator. This is a Streamlit feature that caches the function's output. The first time the function is called, it runs and its result is stored. On subsequent runs (like when a slider is moved), if the function's inputs haven't changed (and in this case, `generate_synthetic_data` has no external inputs), Streamlit serves the result from the cache instead of re-running the code. This makes the app much faster.

### Calculation Logic (`calculate_vsm_performance`)

```python
# application_pages/simulation.py (within calculate_vsm_performance)
@st.cache_data
def calculate_vsm_performance(data, user_policy_clarity, user_intel_strength, user_coordination_level, user_control_effectiveness, user_feedforward_strength, user_feedback_strength, user_governance_style):
    """Calculates Risk Mitigation Effectiveness and Operational Efficiency based on VSM parameters."""
    # Input validation (good practice!)
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input data must be a pandas DataFrame.")
    if user_governance_style not in ['Reactive', 'Preventative', 'Active']:
        raise ValueError("Invalid governance style. Must be 'Reactive', 'Preventative', or 'Active'.")

    processed_data = data.copy()

    # Map Risk Severity to a numeric value
    severity_map = {'Low': 0.2, 'Medium': 0.5, 'High': 1.0}
    processed_data['Risk_Severity_Numeric'] = processed_data['Risk_Severity'].map(severity_map)

    # Calculate Risk Mitigation Effectiveness (RME)
    # This is a simple average of user-input component strengths
    processed_data['Risk_Mitigation_Effectiveness'] = (
        user_policy_clarity +
        user_intel_strength +
        user_coordination_level +
        user_control_effectiveness +
        user_feedforward_strength +
        user_feedback_strength
    ) / 6

    # Calculate Operational Efficiency based on governance style and risk severity
    if user_governance_style == 'Reactive':
        # Higher penalty for risk events
        processed_data['Operational_Efficiency'] = processed_data['Operational_Efficiency_Baseline'] * (1 - 0.1 * processed_data['Risk_Severity_Numeric'])
    elif user_governance_style == 'Preventative':
        # Moderate penalty
        processed_data['Operational_Efficiency'] = processed_data['Operational_Efficiency_Baseline'] * (1 - 0.05 * processed_data['Risk_Severity_Numeric'])
    else: # 'Active'
        # Lower penalty
        processed_data['Operational_Efficiency'] = processed_data['Operational_Efficiency_Baseline'] * (1 - 0.025 * processed_data['Risk_Severity_Numeric'])

    # Drop the intermediate numeric severity column
    return processed_data.drop(columns=['Risk_Severity_Numeric'])
```

*   This function takes the synthetic `data` DataFrame and the user's selected VSM component strengths and governance style as inputs.
*   It first validates the inputs.
*   It maps the categorical `Risk_Severity` ('Low', 'Medium', 'High') to numerical values (`Risk_Severity_Numeric`) that can be used in calculations.
*   It calculates `Risk_Mitigation_Effectiveness` by taking the simple average of the six user-provided VSM component strength values. This value is the same for all rows in the DataFrame because the user inputs are constant across the simulation period.
*   It calculates `Operational_Efficiency` for each row. This calculation starts with the `Operational_Efficiency_Baseline` for that specific row and applies a penalty based on the `Risk_Severity_Numeric` *if* a risk event occurred (implicitly, as `Risk_Severity_Numeric` is only non-zero for risk event rows). The size of this penalty is controlled by the `Risk Impact Factor`, which changes depending on the `user_governance_style` selected in the sidebar.
*   It uses `@st.cache_data` again. This time, the cache depends on the *inputs* to the function (`data`, `user_policy_clarity`, etc.). If you change any slider or the governance style, the function re-runs. If you change something else (like the page), and then come back with the *same* slider values, the result is served from the cache.

### Streamlit UI (`run_simulation`)

```python
# application_pages/simulation.py (within run_simulation)
def run_simulation():
    st.header("VSM Simulation") # Page header

    # Generate data (cached)
    synthetic_data = generate_synthetic_data()

    # Add sidebar controls (these update st.session_state, triggering rerun)
    st.sidebar.header("VSM Component Strengths")
    user_policy_clarity = st.sidebar.slider("Policy Clarity", 0.0, 1.0, 0.5, help="...")
    # ... other sliders
    st.sidebar.header("Governance Style")
    user_governance_style = st.sidebar.selectbox("Select Governance Style", ['Reactive', 'Preventative', 'Active'], help="...")

    # Calculate performance based on data and user inputs (cached based on inputs)
    performance_df = calculate_vsm_performance(
        synthetic_data, user_policy_clarity, user_intel_strength, user_coordination_level,
        user_control_effectiveness, user_feedforward_strength, user_feedback_strength, user_governance_style
    )

    # Display average metrics
    avg_risk_mitigation = performance_df['Risk_Mitigation_Effectiveness'].mean()
    avg_operational_efficiency = performance_df['Operational_Efficiency'].mean()
    st.metric(label="Average Risk Mitigation Effectiveness", value=f"{avg_risk_mitigation:.2f}")
    st.metric(label="Average Operational Efficiency", value=f"{avg_operational_efficiency:.2f}")

    # Create and display charts
    fig_trend = px.line(...) # Time series plot
    st.plotly_chart(fig_trend, use_container_width=True)

    avg_oe_by_severity = performance_df.groupby('Risk_Severity')['Operational_Efficiency'].mean().reset_index()
    fig_oe_severity = px.bar(...) # OE by severity plot
    st.plotly_chart(fig_oe_severity, use_container_width=True)

    avg_rme_by_severity = performance_df.groupby('Risk_Severity')['Risk_Mitigation_Effectiveness'].mean().reset_index()
    fig_rme_severity = px.bar(...) # RME by severity plot
    st.plotly_chart(fig_rme_severity, use_container_width=True)

    # Expander for raw data
    with st.expander("Show Raw Data"):
        st.write(performance_df.head())

```

*   This function defines the layout and content of the Simulation page.
*   It first calls `generate_synthetic_data()` to get the base data.
*   It defines the sidebar widgets (`st.sidebar.slider`, `st.sidebar.selectbox`) that capture user inputs. When a user interacts with a widget, Streamlit automatically re-runs the script from top to bottom.
*   It calls `calculate_vsm_performance()`, passing the synthetic data and the values from the user input widgets. Because of `@st.cache_data`, this calculation only happens if the inputs change.
*   It then calculates the overall averages from the resulting `performance_df`.
*   It uses `plotly.express` to create the required charts based on the `performance_df`.
*   Finally, it uses Streamlit commands (`st.metric`, `st.plotly_chart`, `st.expander`, `st.write`) to display the calculated metrics, the charts, and the raw data on the page. `use_container_width=True` makes the charts responsive.

### Simulation Flow Diagram

This diagram illustrates the flow of data and logic specifically within the Simulation page:

```mermaid
graph TD
    A[Streamlit App Entry] --> B(run_simulation() called)
    B --> C(generate_synthetic_data() - cached)
    B --> D(User interacts with Sidebar Sliders/Selectbox)
    C --> E(Data: synthetic_data)
    D --> E(Inputs: user_policy_clarity, ..., user_governance_style)
    E --> F(calculate_vsm_performance() - cached)
    F --> G(Calculated DataFrame: performance_df)
    G --> H(Calculate Averages)
    G --> I(Generate Plots using Plotly)
    G --> J(Prepare Raw Data Display)
    H --> K(Display Metrics - st.metric)
    I --> L(Display Plots - st.plotly_chart)
    J --> M(Display Raw Data - st.expander, st.write)
    K --> N(Streamlit UI)
    L --> N(Streamlit UI)
    M --> N(Streamlit UI)
```

This diagram shows how the synthetic data and user inputs feed into the calculation function, and how the results are then used by Streamlit to display the key performance indicators and visualizations on the page. The caching layers (`st.cache_data` on steps C and F) are key to the responsiveness of the interactive elements.

Understanding these components provides a clear picture of how the simulation works and how changing inputs impacts the outputs based on the defined formulas and logic.

## Exploring the About Page
Duration: 0:03:00

Finally, let's quickly look at the "About" page.

Navigate to the "About" page by selecting "About" from the "Navigation" selectbox in the sidebar.

This page is generated by the `run_about()` function in `application_pages/about.py`.

```python
# application_pages/about.py
import streamlit as st

def run_about():
    st.title("About Risk Governance Navigator")
    st.markdown("""
    This application is designed to provide an interactive learning and simulation environment for exploring concepts related to risk governance, particularly through the lens of Stafford Beer's Viable System Model (VSM).

    **Viable System Model (VSM)**

    The Viable System Model (VSM) is a cybernetic model developed by Stafford Beer... (rest of the explanation)
    """)
```

This page provides a static explanation of the Viable System Model, outlining its purpose and its five interconnected systems:

*   System 1: Implementation (Primary Activities)
*   System 2: Coordination
*   System 3: Control
*   System 4: Intelligence
*   System 5: Policy

While the application's simulation focuses on the combined impact of elements like Policy, Intelligence, Coordination, Control, and feedback/feedforward loops (which relate to System 3 and System 4 interactions), the About page provides a basic overview of the VSM framework itself, adding context to the concepts explored in the lab.

This page serves as a helpful reference for users less familiar with the VSM.

## Conclusion and Next Steps
Duration: 0:05:00

Congratulations! You have successfully set up and explored the Risk Governance Navigator Streamlit application.

In this codelab, you have:
*   Learned about the importance of risk governance and the relevance of the Viable System Model (VSM).
*   Understood the calculation of key risk governance metrics: Risk Mitigation Effectiveness and Operational Efficiency.
*   Set up and run a multi-page Streamlit application.
*   Interacted with a simulation that allows you to model the impact of VSM component strengths and governance styles.
*   Gained insight into the Python code powering the data generation, calculation, and Streamlit UI.

This application provides a simplified model to illustrate powerful concepts. The core idea is that a well-structured system (like one designed using VSM principles) with appropriate governance mechanisms can significantly improve an organization's ability to manage risk and maintain operational stability, especially in the face of disruptive events.

**Potential Next Steps:**

*   **Modify the synthetic data:** Experiment with the `generate_synthetic_data` function. Could you add more types of risk events? Vary the frequency or severity patterns?
*   **Refine the calculation logic:** How else could `Risk Mitigation Effectiveness` be calculated? Could individual VSM components have a non-linear impact? Could `Operational Efficiency` calculation be made more complex, perhaps considering recovery time after a risk event?
*   **Add more visualizations:** Can you think of other ways to visualize the data or the relationship between VSM parameters and outcomes?
*   **Implement more VSM concepts:** Could you model the interactions *between* VSM systems (e.g., the Algedonic channel between System 1 and System 3)?

By modifying and expanding this application, you can deepen your understanding of both risk governance concepts and Streamlit development.

<aside class="positive">
The code is a great starting point for further experimentation. Feel free to modify the Python files and see how your changes affect the application's behavior. Remember Streamlit automatically updates when you save the file.
</aside>

Thank you for participating in this codelab! We hope it has provided valuable insights into risk governance simulation using the Viable System Model and Streamlit.

