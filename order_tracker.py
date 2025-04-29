
import pandas as pd

# Load data
df = pd.read_csv('sample_data.csv')

# Ensure Total is correct
df['Total'] = df['Quantity'] * df['Price']

# Normalize Payment Status (capitalize)
df['Payment Status'] = df['Payment Status'].str.capitalize()

# Output to cleaned file
df.to_csv('order_summary_cleaned.csv', index=False)

print("✅ Order data processed and saved to 'order_summary_cleaned.csv'")
