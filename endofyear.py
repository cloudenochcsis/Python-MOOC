import csv

def analyze_spendings(csv_file):
    try:
        # Initialize totals
        total_amount = 0
        total_fee = 0
        total_e_levy = 0
        grand_total = 0

        # Open and read the CSV file
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)

            # Ensure the required columns are present
            required_columns = {"amount", "fee", "e-levy", "total"}
            if not required_columns.issubset(set(column.lower() for column in reader.fieldnames)):
                raise ValueError(f"CSV file must contain the columns: {required_columns}")

            for row in reader:
                try:
                    # Sum up the relevant columns
                    total_amount += float(row['amount'])
                    total_fee += float(row['fee'])
                    total_e_levy += float(row['e-levy'])
                    grand_total += float(row['total'])
                except ValueError as e:
                    print(f"Skipping invalid row: {row} - {e}")

        # Print the results
        print(f"Total Amount: ${total_amount:.2f}")
        print(f"Total Fee: ${total_fee:.2f}")
        print(f"Total E-Levy: ${total_e_levy:.2f}")
        print(f"Grand Total: ${grand_total:.2f}")
    
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
csv_file_path = "your_spendings.csv"  # Replace with the path to your CSV file
analyze_spendings(csv_file_path)
