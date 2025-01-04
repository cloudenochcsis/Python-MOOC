import pandas as pd

def analyze_totals(file_path):
    """
    Calculate the sum of each monetary column using raw data.
    """
    # Read the CSV file without any data cleaning
    df = pd.read_csv(file_path)
    
    # Calculate sums directly from the raw columns
    sums = {
        'Amount': df['Amount'].sum(),
        'Fee': df['Fee'].sum(),
        'e-Levy': df['e-Levy'].sum(),
        'Total': df['Total'].sum()
    }
    
    return sums

def print_totals(sums):
    """Print just the total for each column."""
    print("\n=== Column Totals ===")
    print(f"Sum of Amount column: {sums['Amount']}")
    print(f"Sum of Fee column: {sums['Fee']}")
    print(f"Sum of e-Levy column: {sums['e-Levy']}")
    print(f"Sum of Total column: {sums['Total']}")

if __name__ == "__main__":
    # Replace with your CSV file path
    file_path = 'spending_data.csv'
    
    try:
        sums = analyze_totals(file_path)
        print_totals(sums)
    except FileNotFoundError:
        print(f"Error: Could not find the file '{file_path}'")
    except Exception as e:
        print(f"An error occurred: {str(e)}")