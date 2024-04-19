import csv
import pandas as pd

def filter_and_update_csv(file_path, new_column_names):
    # Read and filter the data using pandas for more concise code
    df = pd.read_csv(file_path, header=1)
    df.dropna(how='any', inplace=True)  # This drops rows where any field is NaN
    
    # Assign new column names
    df.columns = new_column_names

    # Save the DataFrame back to the same CSV, effectively updating it
    df.to_csv(file_path, index=False)

# Define the new column names
new_column_names = ['Country', 'ISO Code', 'Year', 'Armed Conflict Deaths', 'Homicide Rate', 'Territorial Control', 'TC Upper Est.', 'TC Lower Est.']

# Usage example
filter_and_update_csv('insecurity_index.csv', new_column_names)
