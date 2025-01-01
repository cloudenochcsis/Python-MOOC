import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict

def analyze_spending(file_path):
    """
    Analyze spending data from a CSV file and generate summary statistics.
    
    Parameters:
    file_path (str): Path to the CSV file containing spending data
    
    Returns:
    dict: Dictionary containing spending analysis results
    """
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Calculate totals
    analysis = {
        'total_amount': df['total'].sum(),
        'total_fees': df['fee'].sum(),
        'total_elevy': df['e-levy'].sum(),
        'transaction_count': len(df),
        
        # Calculate spending by service
        'spending_by_service': df.groupby('service')['total'].sum().sort_values(ascending=False),
        
        # Calculate spending by payment method
        'spending_by_payment': df.groupby('payment method')['total'].sum(),
        
        # Monthly spending trend
        'monthly_spending': df.assign(
            month=pd.to_datetime(df['Date']).dt.strftime('%Y-%m')
        ).groupby('month')['total'].sum()
    }
    
    # Calculate percentages for major spending categories
    total_spent = analysis['total_amount']
    analysis['service_percentages'] = (analysis['spending_by_service'] / total_spent * 100).round(2)
    
    return analysis

def print_analysis(analysis):
    """Print the analysis results in a readable format."""
    print("\n=== Spending Analysis Summary ===")
    print(f"\nTotal Amount Spent: {analysis['total_amount']:.2f}")
    print(f"Total Fees: {analysis['total_fees']:.2f}")
    print(f"Total E-Levy: {analysis['total_elevy']:.2f}")
    print(f"Number of Transactions: {analysis['transaction_count']}")
    
    print("\n=== Top Spending Categories ===")
    for service, percentage in analysis['service_percentages'].head().items():
        print(f"{service}: {percentage}% ({analysis['spending_by_service'][service]:.2f})")
    
    print("\n=== Monthly Spending Trend ===")
    for month, amount in analysis['monthly_spending'].items():
        print(f"{month}: {amount:.2f}")

if __name__ == "__main__":
    # Replace 'spending_data.csv' with your CSV file path
    file_path = 'spending_data.csv'
    
    try:
        analysis_results = analyze_spending(file_path)
        print_analysis(analysis_results)
    except FileNotFoundError:
        print(f"Error: Could not find the file '{file_path}'")
    except Exception as e:
        print(f"An error occurred: {str(e)}")