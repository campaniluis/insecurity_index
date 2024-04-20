import pandas as pd

# Step 1: Load data from CSV
df = pd.read_csv('output_data/insecurity_index.csv')

# Step 2: Define the calculation for the new column
df['Score'] = df['Homicide Rate'] ** (df['Territorial Control'] + df['Armed Conflict Deaths'] + 1)

# Step 4: Save the updated DataFrame back to a new CSV file
df.to_csv('output_data/insecurity_index.csv', index=False)

# , 'Homicide Rate', , 'TC Upper Est.', 'TC Lower Est.']