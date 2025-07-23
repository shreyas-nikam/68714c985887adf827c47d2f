# QuLab: Operational Risk Measurement


## Description

This lab is a Streamlit-based interactive lab designed to explore various operational risk measurement approaches. It provides hands-on tools for data validation, comparative analysis against benchmarks, visualization of risk profiles, and analysis of cost variability within trading operations.



## Features

*   **Data Loading & Summary**:
    *   Upload trading data via CSV.
    *   Automated validation for required columns (`Date`, `Cost per Trade`, `Trade ID`, `Risk Category`, `Severity`, `Likelihood`, `Firm Type`) and data types.
    *   Handles missing data warnings.
    *   Provides summary statistics (`.describe()`) and data type information.
    *   Includes sample data if no file is uploaded.
*   **Comparative Analysis**:
    *   Benchmark your firm's operational risk management quality against a peer or standard.
    *   Compare scores across key quality areas: Output, Process, Audience, and Success.
    *   Visualizes comparisons using an intuitive side-by-side bar chart.
*   **Risk Profile Grid**:
    *   Interactively plot individual risks on a Likelihood vs. Severity matrix.
    *   Visualize risks categorized into four strategic quadrants: Ignore, Monitor, Cost, and Strategic Risk.
    *   Helps in prioritizing risks based on their position on the grid.
*   **Cost Variability Analysis**:
    *   Calculate the Normalized Standard Deviation of 'Cost per Trade'.
    *   Uses the formula: $\frac{\sigma_{\text{cost per trade}}}{\text{Max Cost per Trade} - \text{Min Cost per Trade}}$.
    *   Can use 'Cost per Trade' data from the uploaded file or manual input.
    *   Provides a metric for monitoring operational efficiency and cost consistency.
*   **Additional Visualizations**:
    *   **Time-based Trend Plot**: Visualize the trend of 'Cost per Trade' over time using a line chart (Plotly).
    *   **Categorical Insights**: Analyze average 'Severity' across different 'Risk Category' using a bar chart (Plotly).

## Getting Started

### Prerequisites

*   Python 3.7 or higher
*   `pip` package installer

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your_username/your_repo_name.git
    cd your_repo_name
    ```
    *(Note: Replace `your_username/your_repo_name.git` with the actual repository URL if this project is hosted on a platform like GitHub.)*

2.  **Install the required packages:**
    It's recommended to install dependencies from a `requirements.txt` file. If you don't have one, create a file named `requirements.txt` in the project root with the following content:
    ```
    streamlit>=1.0
    pandas
    numpy
    matplotlib
    plotly
    ```
    Then, install the packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the Streamlit application:**
    Navigate to the root directory of the project (where `app.py` is located) in your terminal.
    ```bash
    streamlit run app.py
    ```

2.  The application will open in your web browser, usually at `http://localhost:8501`.

3.  **Navigate the App:**
    *   Use the sidebar on the left to select different analysis pages: "Data Loading & Summary", "Comparative Analysis", "Risk Profile Grid", "Cost Variability Analysis", "Additional Visualizations".
    *   **Data Loading & Summary**: Start here. Upload your CSV data containing the required columns. If no file is uploaded, sample data will be used. The loaded data (or sample data) is used by subsequent pages.
    *   Explore the different pages and interact with the widgets (sliders, number inputs, text inputs, checkboxes) to see the results and visualizations.

## Project Structure

```
.
├── app.py
├── requirements.txt  # (Recommended, if not already present)
└── application_pages/
    ├── __init__.py
    ├── data_loading.py
    ├── comparative_analysis.py
    ├── risk_profile.py
    ├── cost_variability.py
    └── additional_visualizations.py
```

*   `app.py`: The main entry point that orchestrates the navigation and loads different application pages.
*   `requirements.txt`: Lists the Python dependencies.
*   `application_pages/`: Directory containing separate Python modules for each section/page of the application.

## Technology Stack

*   **Framework**: Streamlit
*   **Data Manipulation**: Pandas
*   **Numerical Operations**: NumPy
*   **Plotting (Static)**: Matplotlib
*   **Plotting (Interactive)**: Plotly
*   **Language**: Python

## Contributing

Contributions are welcome! If you find a bug or have a suggestion for improvement, please:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes and commit them (`git commit -m 'Add new feature'`).
4.  Push to your fork (`git push origin feature/your-feature-name`).
5.  Create a Pull Request to the main repository.

## License

This project is licensed under the [Specify Your License Here, e.g., MIT License]. See the `LICENSE` file (if available) for details.

## Contact

If you have any questions or feedback, you can reach out to:

*   [Your Name/Organization Name]
*   [Your Email Address]
*   [Link to Project Repository or Website]
