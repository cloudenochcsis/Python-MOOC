import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# --- Configuration ---
INPUT_FILE = 'performance_data.csv'
OUTPUT_BAR_CHART = 'performance_bar_chart.png'
OUTPUT_BOX_PLOT = 'performance_box_plot.png'

# --- Main Script ---

def generate_graphs(data_df):
    """Generates and saves the performance graphs."""

    # Set the style for the plots
    sns.set_style("whitegrid")

    # --- 1. Bar Chart for Average Latency ---
    plt.figure(figsize=(12, 7))
    bar_plot = sns.barplot(
        x='SearchType',
        y='AverageLatency',
        hue='Explorer',
        data=data_df,
        palette='viridis'
    )
    plt.title('Average Search Latency by Block Explorer', fontsize=16)
    plt.xlabel('Search Type', fontsize=12)
    plt.ylabel('Average Latency (ms)', fontsize=12)
    plt.xticks(rotation=0)
    plt.legend(title='Explorer')
    
    # Add labels to the bars
    for p in bar_plot.patches:
        bar_plot.annotate(format(p.get_height(), '.1f'), 
                       (p.get_x() + p.get_width() / 2., p.get_height()), 
                       ha = 'center', va = 'center', 
                       xytext = (0, 9), 
                       textcoords = 'offset points')

    plt.tight_layout()
    plt.savefig(OUTPUT_BAR_CHART)
    print(f"Bar chart saved to {OUTPUT_BAR_CHART}")

    # --- 2. Box Plot for Latency Distribution (with simulated data) ---
    # We need to generate some sample data for the box plot, as we only have averages.
    np.random.seed(42)
    box_plot_data = []
    for index, row in data_df.iterrows():
        # Generate 20 data points around the average latency
        # with a realistic standard deviation.
        simulated_latencies = np.random.normal(
            loc=row['AverageLatency'], 
            scale=row['AverageLatency']*0.1, # 10% standard deviation
            size=20
        )
        for latency in simulated_latencies:
            box_plot_data.append({
                'Explorer': row['Explorer'],
                'SearchType': row['SearchType'],
                'Latency': latency
            })
    
    box_df = pd.DataFrame(box_plot_data)

    plt.figure(figsize=(12, 7))
    sns.boxplot(
        x='SearchType',
        y='Latency',
        hue='Explorer',
        data=box_df,
        palette='viridis'
    )
    plt.title('Simulated Latency Distribution by Block Explorer', fontsize=16)
    plt.xlabel('Search Type', fontsize=12)
    plt.ylabel('Latency (ms)', fontsize=12)
    plt.xticks(rotation=0)
    plt.legend(title='Explorer')
    plt.tight_layout()
    plt.savefig(OUTPUT_BOX_PLOT)
    print(f"Box plot saved to {OUTPUT_BOX_PLOT}")


if __name__ == "__main__":
    try:
        # Read the performance data
        performance_data = pd.read_csv(INPUT_FILE)
        
        # Generate the graphs
        generate_graphs(performance_data)

    except FileNotFoundError:
        print(f"Error: The input file '{INPUT_FILE}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
