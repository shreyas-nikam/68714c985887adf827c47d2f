import pandas as pd
import os

def load_and_validate_data(filepath=None):
    """Loads, validates, and summarizes data."""
    if filepath is None:
        data = {'Date': ['2024-01-01'], 'Cost per Trade': [1.0], 'Trade ID': [1], 'Risk Category': ['dummy'], 'Severity': [1], 'Likelihood': [1], 'Firm Type': ['A']}
        df = pd.DataFrame(data)
    else:
        try:
            df = pd.read_csv(filepath)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {filepath}")

    required_columns = ['Date', 'Cost per Trade', 'Trade ID', 'Risk Category', 'Severity', 'Likelihood', 'Firm Type']
    for col in required_columns:
        if col not in df.columns:
            raise KeyError(f"Missing column: {col}")

    try:
        df['Date'] = pd.to_datetime(df['Date'])
        df['Cost per Trade'] = pd.to_numeric(df['Cost per Trade'])
        df['Trade ID'] = pd.to_numeric(df['Trade ID'], downcast='integer')
        df['Severity'] = pd.to_numeric(df['Severity'], downcast='integer')
        df['Likelihood'] = pd.to_numeric(df['Likelihood'], downcast='integer')
    except ValueError:
        raise ValueError("Invalid data type in DataFrame")

    print(df.describe())
    print(df.dtypes)

    return df

import matplotlib.pyplot as plt

def perform_comparative_analysis(firm_scores, benchmark_scores):
    """Compares firm scores against benchmark scores."""

    categories = list(firm_scores.keys())
    firm_values = list(firm_scores.values())
    benchmark_values = list(benchmark_scores.values())

    x = range(len(categories))
    width = 0.35

    plt.figure(figsize=(10, 6))
    plt.bar([i - width/2 for i in x], firm_values, width, label='Firm')
    plt.bar([i + width/2 for i in x], benchmark_values, width, label='Benchmark')

    plt.xlabel('Quality Areas')
    plt.ylabel('Scores')
    plt.title('Comparative Analysis of Firm vs Benchmark')
    plt.xticks(x, categories)
    plt.legend()
    plt.tight_layout()  # Adjust layout to prevent labels from overlapping
    plt.show()

import matplotlib.pyplot as plt

def plot_risk_profile(severity, likelihood, risk_name):
    """Plots a risk on a scatter plot."""

    plt.figure(figsize=(8, 6))
    plt.scatter(likelihood, severity, marker='o', s=100, label=risk_name)

    plt.xlabel("Likelihood")
    plt.ylabel("Severity")
    plt.title("Risk Profile")

    plt.xlim(0, 10)
    plt.ylim(0, 10)

    plt.axvline(x=5, color='black', linestyle='--', linewidth=0.5)
    plt.axhline(y=5, color='black', linestyle='--', linewidth=0.5)

    plt.text(2.5, 2.5, "Ignore", fontsize=12, ha='center', va='center')
    plt.text(7.5, 2.5, "Monitor", fontsize=12, ha='center', va='center')
    plt.text(2.5, 7.5, "Cost", fontsize=12, ha='center', va='center')
    plt.text(7.5, 7.5, "Strategic Risk", fontsize=12, ha='center', va='center')

    plt.legend()
    plt.grid(True)
    plt.show()

import numpy as np

def calculate_normalized_std_dev(cost_data):
    """Calculates the normalized standard deviation of cost per trade."""
    if not cost_data:
        raise ZeroDivisionError("Cost data cannot be empty.")

    if len(cost_data) <= 1:
        return 0.0

    std_dev = np.std(cost_data)
    data_range = max(cost_data) - min(cost_data)

    if data_range == 0:
        return 0.0

    return std_dev / data_range