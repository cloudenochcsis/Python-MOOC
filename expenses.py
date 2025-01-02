import pandas as pd

# Read the CSV file
df = pd.read_csv('spending_data.csv')

# Convert currency columns from string to float, removing 'GHS ' prefix
currency_columns = ['Amount', 'Fee', 'e-Levy', 'Total']
for col in currency_columns:
    df[col] = df[col].str.replace('GHS ', '').astype(float)

# Calculate sums
total_amount = df['Amount'].sum()
total_fee = df['Fee'].sum()
total_elevy = df['e-Levy'].sum()
total_sum = df['Total'].sum()

# Print results
print(f"Total Amount: GHS {total_amount:.2f}")
print(f"Total Fee: GHS {total_fee:.2f}")
print(f"Total e-Levy: GHS {total_elevy:.2f}")
print(f"Total Sum: GHS {total_sum:.2f}")