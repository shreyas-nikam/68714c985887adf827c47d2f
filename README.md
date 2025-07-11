# Risk Governance Navigator (QuLab Project)

## Project Title

**Risk Governance Navigator**

## Description

The **Risk Governance Navigator** is a Streamlit-based lab project designed to provide an interactive exploration of risk governance concepts, specifically leveraging Stafford Beer's **Viable System Model (VSM)**.

This application allows users to simulate and visualize how different organizational governance styles (Reactive, Preventative, Active) and the perceived effectiveness of key VSM components impact an organization's **Risk Mitigation Effectiveness** and **Operational Efficiency**. It aims to provide a practical demonstration of theoretical concepts from operational risk management literature, helping users understand the tangible effects of strategic governance choices on organizational resilience and performance.

Built as part of the QuLab initiatives, this tool serves as an educational resource to deepen understanding of complex risk governance dynamics.

## Features

*   **Interactive VSM Parameter Adjustment**: Use sliders in the sidebar to set the perceived strength/effectiveness of key VSM components (Policy Clarity, Intelligence Strength, Coordination Level, Control Effectiveness, Feedforward Strength, Feedback Strength).
*   **Governance Style Selection**: Choose between Reactive, Preventative, and Active governance styles to see their differential impact on performance, especially during risk events.
*   **Real-time Metric Display**: View the calculated average **Risk Mitigation Effectiveness** and **Operational Efficiency** metrics based on your chosen parameters and governance style.
*   **Performance Trend Visualization**: See how Operational Efficiency and Risk Mitigation Effectiveness evolve over simulated time using interactive line charts.
*   **Impact Analysis by Risk Severity**: Visualize the average performance metrics broken down by different risk severity levels (Low, Medium, High) using bar charts.
*   **Conceptual Overview**: Learn about the theoretical underpinnings of the Viable System Model and the calculation methodologies for the performance metrics via the "Overview" page.
*   **Multi-Page Navigation**: Easily navigate between the Overview, Simulation, and About sections using a sidebar menu.
*   **About Section**: Get a brief introduction to the Viable System Model's five systems.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python 3.7 or higher
*   `pip` package installer

### Installation

1.  Clone the repository (assuming the code is hosted in a Git repository):

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
    *(Replace `<repository_url>` and `<repository_directory>` with the actual details of your project's repository)*

2.  Navigate into the application_pages directory and ensure an empty `__init__.py` file exists if you are putting the code into a fresh structure:

    ```bash
    mkdir application_pages
    touch application_pages/__init__.py
    # Copy the overview.py, simulation.py, and about.py files into application_pages/
    ```

3.  Create a `requirements.txt` file in the root directory of the project and add the necessary libraries:

    ```text
    streamlit>=1.0
    pandas
    numpy
    plotly
    ```

4.  Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the application, open your terminal or command prompt, navigate to the project's root directory (where `app.py` is located), and execute the following command:

```bash
streamlit run app.py
```

This will open the application in your default web browser.

*   Use the sidebar navigation to switch between "Overview", "Simulation", and "About" pages.
*   On the "Simulation" page, use the sliders and selectbox in the **sidebar** to adjust VSM component strengths and the governance style. Observe how the average metrics and charts update in real-time.

## Project Structure

```text
.
├── app.py                       # Main Streamlit application entry point
├── requirements.txt             # List of required Python packages
└── application_pages/           # Directory containing individual page scripts
    ├── __init__.py              # Makes the directory a Python package
    ├── overview.py              # Script for the 'Overview' page (VSM concepts, metrics explanation)
    ├── simulation.py            # Script for the 'Simulation' page (interactive sliders, calculations, charts)
    └── about.py                 # Script for the 'About' page (VSM general info)
```

## Technology Stack

*   **Core Application Framework**: Streamlit
*   **Data Handling**: Pandas, NumPy
*   **Visualization**: Plotly Express
*   **Language**: Python 3

## Contributing

This project is primarily intended as a lab exercise. However, if you have suggestions for improvements or find issues, feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeature`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some feature'`).
5.  Push to the branch (`git push origin feature/YourFeature`).
6.  Open a Pull Request.

Please ensure your code adheres to standard Python practices and includes necessary documentation or tests if applicable.

## License

This project is licensed under the MIT License - see the LICENSE.md file (if available) for details. If no specific LICENSE.md is provided, consider it released under a standard open-source license suitable for educational projects.

## Contact

For questions or inquiries related to this project, please contact:

*   [Your Name/Organization Name]
*   [Your Email Address or Link to Website/Profile]
    *(Relevant link based on the logo: [QuantUniversity](https://www.quantuniversity.com/))*

---

*This README was generated based on the provided Streamlit application code.*
