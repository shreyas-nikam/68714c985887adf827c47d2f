id: 68714c985887adf827c47d2f_user_guide
summary: Risk Governance Lab 2 User Guide
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Explore Risk Governance with the VSM Navigator

## Introduction to Risk Governance and the VSM Navigator
Duration: 05:00

Welcome to the **Risk Governance Navigator Lab**!

Modern organizations operate in dynamic and unpredictable environments, constantly facing various forms of risk. Effective risk governance is not just about reacting to problems when they occur, but about building resilient systems that can anticipate, prevent, and mitigate risks proactively while maintaining operational efficiency.

This application introduces the **Viable System Model (VSM)**, a powerful framework developed by Stafford Beer, which provides a cybernetic lens to view and design organizations. The VSM emphasizes the interconnectedness of different organizational functions and their information flows necessary for long-term survival and adaptation. By understanding the VSM, organizations can better structure their governance mechanisms to handle complexity and uncertainty.

In this lab, you will use the **Risk Governance Navigator** application to:

*   Understand the core concepts of the Viable System Model (VSM).
*   Explore different styles of risk governance: **Reactive**, **Preventative**, and **Active**.
*   Visualize how adjusting the effectiveness of VSM components and selecting different governance styles impacts key performance indicators like **Risk Mitigation Effectiveness** and **Operational Efficiency**.

The application uses a simplified simulation model to demonstrate these concepts. By interacting with the application, you will gain practical insights into how theoretical governance frameworks translate into measurable outcomes.

We will also look at how two key metrics, **Risk Mitigation Effectiveness** and **Operational Efficiency**, are calculated within this simulation.

**Risk Mitigation Effectiveness** is calculated as the average of the effectiveness scores assigned to key VSM components:

$$
\text{Risk Mitigation Effectiveness} = \frac{\text{Policy Clarity} + \text{Intelligence Strength} + \text{Coordination Level} + \text{Control Effectiveness} + \text{Feedforward Strength} + \text{Feedback Strength}}{6}
$$

This metric gives a holistic view of the system's inherent capability to manage and reduce risks based on the strength of its governance elements.

**Operational Efficiency** reflects how smoothly operations run, taking into account the baseline efficiency and any impact from risk events, moderated by the chosen governance style.

$$
\text{Operational Efficiency} = \text{Operational Efficiency Baseline} \times (1 - \text{Risk Impact Factor} \times \text{Risk Severity})
$$

The **Risk Impact Factor** is crucial here, as it changes depending on whether the governance style is Reactive, Preventative, or Active. A Reactive style assumes a higher negative impact on efficiency when a risk occurs compared to a Preventative or Active style, even if the risk severity is the same. This highlights how proactive governance can cushion the blow of risk events.

Let's start navigating the application to explore these ideas further.

## Navigating the Application
Duration: 02:00

The application is structured into three main sections, accessible via the sidebar navigation on the left.

1.  **Overview:** This is the starting page. It provides an introduction to the application's purpose, the business value of effective risk governance using VSM, what you will learn, and details the calculation of the key performance metrics.
2.  **Simulation:** This is the interactive heart of the application. Here, you can adjust various parameters related to VSM components and governance styles and observe their impact on simulated performance data.
3.  **About:** This page provides a more detailed explanation of the Viable System Model (VSM) itself, outlining its five main systems and their roles in a viable organization.

To navigate between these sections, simply use the **"Navigation"** dropdown menu located in the sidebar.

<aside class="positive">
Try switching between the **Overview**, **Simulation**, and **About** pages using the sidebar now. Notice how the main content area changes to reflect the selected page.
</aside>

The sidebar also contains the application's logo and title. On the "Simulation" page, the sidebar will contain additional controls that allow you to interact with the simulation parameters.

## Exploring the Overview and About Pages
Duration: 03:00

Before diving into the simulation, take some time to read the content on the **Overview** and **About** pages.

*   **Overview Page:** Review the "Business Value" and "What You'll Learn" sections to solidify your understanding of why risk governance and the VSM are important and what you can expect to gain from using the application. Pay special attention to the sections explaining the **Risk Mitigation Effectiveness** and **Operational Efficiency** calculations, including the mathematical formulas. This will help you interpret the results in the simulation later.
*   **About Page:** Read the explanation of the **Viable System Model (VSM)** and its five interconnected systems (System 1 through System 5). Try to relate these systems to the VSM component names you saw mentioned in the Overview (Policy, Intelligence, Coordination, Control, Feedforward, Feedback). Understanding the VSM structure provides context for the simulation parameters you will adjust.

<aside class="positive">
Make sure you understand the basic definitions of the VSM systems and the two performance metrics before moving to the simulation.
</aside>

These pages provide the foundational knowledge needed to fully appreciate the simulation results.

## Running the Simulation
Duration: 10:00

Now, navigate to the **Simulation** page using the sidebar.

This page allows you to simulate the impact of different risk governance approaches based on the VSM framework.

On this page, you will see:

*   Headers displaying **Average Risk Mitigation Effectiveness** and **Average Operational Efficiency**.
*   Charts visualizing **Performance Trends Over Time** and aggregated performance by **Risk Severity**.
*   An expander to view **Raw Data**.

Crucially, the **sidebar** changes on this page. It now contains controls grouped under "VSM Component Strengths" and "Governance Style".

*   **VSM Component Strengths:** These are sliders that let you adjust the perceived effectiveness of different VSM elements within the simulated system. For example, increasing the "Policy Clarity" slider simulates having clearer, more effective policies. Each slider ranges from $0.0$ (lowest effectiveness) to $1.0$ (highest effectiveness).
*   **Governance Style:** This is a dropdown menu allowing you to select one of three governance styles: **Reactive**, **Preventative**, or **Active**.

<aside class="positive">
Start by keeping the VSM Component Strengths at their default mid-range values ($0.5$). Select the **Reactive** governance style from the dropdown.
</aside>

As you adjust the sliders or change the governance style, the application automatically recalculates the performance metrics and updates the charts based on synthetic data generated for the simulation.

Experiment with the sliders:
*   What happens to the **Average Risk Mitigation Effectiveness** when you increase all VSM component strengths towards $1.0$?
*   What happens when you decrease them towards $0.0$?
*   Observe the **Operational Efficiency** average and trend line.

Now, try changing the **Governance Style**:
*   Select **Preventative**. How do the metrics, especially Operational Efficiency, change compared to **Reactive**?
*   Select **Active**. How does this compare to the other two styles?

Pay close attention to how Operational Efficiency is affected, particularly as shown in the "Average Operational Efficiency by Risk Severity" bar chart. Remember the formula from the Overview page and how the `Risk Impact Factor` changes with the governance style.

## Interpreting Simulation Results
Duration: 10:00

Understanding the charts and metrics is key to deriving insights from the simulation.

*   **Average Metrics:** The two average metrics at the top give you a quick summary of overall performance under the current settings. Higher numbers are generally better.
*   **Performance Trends Over Time:** This line chart shows how both Operational Efficiency and Risk Mitigation Effectiveness evolve over the simulated time period.
    *   Notice that Risk Mitigation Effectiveness remains constant if you don't change the VSM component sliders, as it's calculated directly from these static inputs.
    *   Operational Efficiency, however, fluctuates. Look closely at points where risk events might be implied (though not explicitly marked in the plot). See how the chosen governance style influences the *level* of the Operational Efficiency line and its dips.
*   **Average Operational Efficiency by Risk Severity:** This bar chart is particularly insightful for understanding the impact of governance style. Under a Reactive style, you should observe a significant drop in average Operational Efficiency for 'High' severity risks compared to 'Low' risks. With Preventative and especially Active styles, this difference should become smaller, demonstrating their buffering effect against severe risks.
*   **Average Risk Mitigation Effectiveness by Risk Severity:** This chart helps reinforce that Risk Mitigation Effectiveness, as calculated here, is primarily a function of the VSM component strengths you set, not the risk severity itself. It shows the *system's capability*, which applies across all risk severities.

<aside class="positive">
Challenge yourself:
1.  Set all VSM component strengths low (e.g., 0.2). Observe the Operational Efficiency for High Severity risks under Reactive governance.
2.  Now, switch to Active governance while keeping VSM component strengths low. Does OE for High Severity risks improve? Why? (Hint: Look at the Operational Efficiency formula and the Risk Impact Factor).
3.  Set all VSM component strengths high (e.g., 0.8). Observe the Operational Efficiency for High Severity risks under Reactive governance.
4.  Now, switch to Active governance with high VSM strengths. How does OE for High Severity risks compare now?

</aside>

Use the "Show Raw Data" expander if you want to see the underlying numbers that generate these charts, including the simulated daily values and calculated metrics.

By actively experimenting with the sliders and the governance style, you can build an intuitive understanding of how different aspects of governance and system design interact to influence an organization's ability to handle risks and maintain efficient operations.

## Understanding the Viable System Model (VSM) Components in the Simulation
Duration: 05:00

Let's tie the VSM concepts from the "About" page back to the simulation controls. The sliders in the sidebar represent the effectiveness of different VSM functions as they relate to risk governance:

*   **Policy Clarity:** Relates to VSM System 5 (Policy). Clear policies define the organization's direction and risk appetite, guiding decisions and actions across all systems. Higher clarity means better alignment and understanding of risk-related rules.
*   **Intelligence Strength:** Relates to VSM System 4 (Intelligence). This is the organization's ability to sense the external environment, identify potential risks, and analyze trends. Strong intelligence provides early warnings and informs strategic adjustments.
*   **Coordination Level:** Relates to VSM System 2 (Coordination). Ensures that different operational units (VSM System 1s) work together effectively, avoiding conflicts and ensuring consistent risk management practices across the organization.
*   **Control Effectiveness:** Relates to VSM System 3 (Control). This system monitors the performance of operational units (System 1s), ensuring they comply with policies and procedures and take corrective action when needed. Effective controls catch issues before they escalate.
*   **Feedforward Strength:** Represents the system's ability to anticipate future conditions and potential risks based on intelligence (System 4) and policy (System 5). It influences proactive measures.
*   **Feedback Strength:** Represents the system's ability to learn from past events (both successes and failures, including risk incidents). Strong feedback loops (involving Systems 3, 4, and 5 interacting with System 1s) enable continuous improvement in risk management processes.

By adjusting these sliders, you are essentially simulating an organization where these VSM functions are more or less effective in supporting risk governance. Higher slider values contribute positively to the overall Risk Mitigation Effectiveness calculation.

The **Governance Style** ('Reactive', 'Preventative', 'Active') represents the overarching meta-system (related to how Systems 3, 4, and 5 interact and prioritize) that dictates the organization's primary approach to risk management. As the simulation shows, this strategic choice significantly impacts how efficiently the organization operates, especially in the face of adverse events.

## Conclusion and Further Exploration
Duration: 02:00

Congratulations! You have successfully navigated the Risk Governance Navigator application and explored key concepts related to risk governance and the Viable System Model.

You have learned:

*   The importance of effective risk governance in modern organizations.
*   The foundational structure of the Viable System Model (VSM).
*   The distinction between Reactive, Preventative, and Active governance styles.
*   How the effectiveness of VSM components contributes to Risk Mitigation Effectiveness.
*   How governance style impacts Operational Efficiency, particularly in the presence of risk events.
*   How to use the application's simulation features and interpret the resulting metrics and charts.

This application provides a simplified model to illustrate complex ideas. Real-world risk governance is far more nuanced, involving human factors, culture, specific industry regulations, and complex interactions not captured here. However, the core principles demonstrated – that system design (VSM component strength) and strategic approach (governance style) are critical determinants of resilience and performance – remain valid.

Feel free to spend more time with the simulation, trying different combinations of VSM component strengths and governance styles to deepen your understanding.

<aside class="positive">
Consider how you might apply these concepts to an organization or system you are familiar with. Which VSM components might need strengthening? What governance style seems most appropriate for its environment and risk profile?
</aside>

We hope this lab has provided valuable insights into the dynamics of risk governance through the lens of the Viable System Model.
