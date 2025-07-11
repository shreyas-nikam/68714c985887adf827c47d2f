import pandas as pd
import os

def load_and_validate_data(file_path, generate_sample):
    """Loads and validates operational loss data."""
    if file_path and os.path.exists(file_path):
        try:
            df = pd.read_csv(file_path)
            # Attempt to convert 'Date' column to datetime objects
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

            # Handle potential parsing errors by coercing invalid dates to NaT.
            # Further processing to address NaT values (e.g., imputation or removal) can be added here
            return df
        except pd.errors.EmptyDataError:
            raise pd.errors.EmptyDataError("The CSV file is empty.")
        except Exception as e:
            print(f"Error loading or processing data: {e}")
            if generate_sample:
                return generate_synthetic_data()  # Generate sample data if loading fails
            else:
                raise  # Re-raise the exception if not generating sample data
    elif generate_sample:
        return generate_synthetic_data()
    else:
        raise FileNotFoundError("File not found and generate_sample is False.")

def generate_synthetic_data():
    """Generates a synthetic dataset."""
    data = {'Incident_ID': [1, 2],
            'Date': ['2023-01-01', '2023-01-02'],
            'Loss_Amount': [100, 200],
            'Business_Unit': ['A', 'B']}
    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

import pandas as pd

def apply_filters(df, start_date, end_date, selected_business_units, selected_event_types, min_loss_amount, max_loss_amount):
    """Applies filters to the DataFrame based on user-selected criteria."""

    if start_date:
        df = df[df['Date'] >= pd.to_datetime(start_date)]
    if end_date:
        df = df[df['Date'] <= pd.to_datetime(end_date)]
    if selected_business_units:
        df = df[df['Business_Unit'].isin(selected_business_units)]
    if selected_event_types:
        df = df[df['Event_Type'].isin(selected_event_types)]
    if min_loss_amount is not None:
        df = df[df['Loss_Amount'] >= min_loss_amount]
    if max_loss_amount is not None:
        df = df[df['Loss_Amount'] <= max_loss_amount]

    return df

import pandas as pd
import matplotlib.pyplot as plt

def plot_loss_trend(df_filtered, granularity):
    """Generates time series plot of loss amounts and incident counts."""
    if df_filtered.empty:
        df_resampled = pd.DataFrame({
            'Loss_Amount': [],
            'Incident_Count': []
        })
    else:
        df_filtered = df_filtered.set_index('Date')
        df_resampled = df_filtered.resample(granularity)[['Loss_Amount', 'Incident_Count']].sum()

    fig, ax1 = plt.subplots(figsize=(12, 6))

    color = 'tab:blue'
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Loss Amount', color=color)
    ax1.plot(df_resampled.index, df_resampled['Loss_Amount'], color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()

    color = 'tab:red'
    ax2.set_ylabel('Incident Count', color=color)
    ax2.plot(df_resampled.index, df_resampled['Incident_Count'], color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.title('Loss Amount and Incident Count Trend')
    plt.show()

import pandas as pd
import matplotlib.pyplot as plt


def plot_frequency_severity(df_filtered, group_by_column):
    """Generates a scatter plot of loss frequency vs. severity."""

    if df_filtered.empty:
        print("DataFrame is empty. No plot to generate.")
        return

    try:
        grouped = df_filtered.groupby(group_by_column).agg(
            {'Loss_Amount': 'sum', 'Incident_Count': 'sum'})

        if grouped.empty:
            print("Grouped DataFrame is empty. No plot to generate.")
            return

        x = grouped['Incident_Count']
        y = grouped['Loss_Amount']

        plt.figure(figsize=(10, 6))
        plt.scatter(x, y, s=100)
        plt.xlabel('Incident Count')
        plt.ylabel('Total Loss Amount')
        plt.title(f'Loss Frequency vs. Severity by {group_by_column}')

        for i, txt in enumerate(grouped.index):
            plt.annotate(txt, (x[i], y[i]), fontsize=9)

        plt.grid(True)
        plt.show()

    except KeyError:
        raise KeyError(f"Column '{group_by_column}' not found in DataFrame.")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_aggregated_comparison(df_filtered, category_column, metric_column):
    """Generates a plot comparing total losses/counts across categories."""
    if df_filtered.empty:
        print("DataFrame is empty. No plot to display.")
        return

    try:
        aggregated_data = df_filtered.groupby(category_column)[metric_column].sum()

        if len(aggregated_data) > 10:
            # Create a heatmap if there are too many categories
            pivot_table = df_filtered.pivot_table(values=metric_column, index=category_column, aggfunc='sum')
            plt.figure(figsize=(10, 8))
            sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt=".1f")
            plt.title(f'Heatmap of Total {metric_column} by {category_column}')
            plt.ylabel(category_column)
            plt.xlabel(metric_column)

        else:
            # Create a bar chart
            aggregated_data.plot(kind='bar', figsize=(10, 6))
            plt.title(f'Total {metric_column} by {category_column}')
            plt.xlabel(category_column)
            plt.ylabel(metric_column)
            plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

    except KeyError:
        raise KeyError(f"Column '{category_column}' or '{metric_column}' not found in DataFrame.")

import pandas as pd
import numpy as np

def calculate_normalized_sd(df_filtered, cost_column):
    """Calculates the normalized standard deviation of a cost column."""
    if df_filtered.empty:
        return np.nan

    mean_cost = df_filtered[cost_column].mean()

    if mean_cost == 0:
        return 0.0
    
    if np.isnan(mean_cost):
        return np.nan

    std_dev_cost = df_filtered[cost_column].std()

    if np.isnan(std_dev_cost):
        return np.nan

    if std_dev_cost == 0 and mean_cost > 0:
        return 0.0
    elif std_dev_cost > 0 and mean_cost == 0:
        return np.inf
    elif std_dev_cost == 0 and mean_cost == 0:
         return np.nan

    normalized_sd = std_dev_cost / mean_cost

    return normalized_sd