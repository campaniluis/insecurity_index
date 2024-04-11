import csv
import pandas as pd

# Define the new column names
new_column_names = ['Country', 'ISO Code', 'Year', 'Armed Conflict Deaths', 'Homicide Rate', 'Territorial Control','TC Upper Est.','TC Lower Est.']

# Load the CSV file with new column names
df = pd.read_csv

# Function to filter the CSV
def filter_csv(concat_index, parsed_index):
    with open(concat_index, mode='r', newline='') as infile, open(parsed_index, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        for row in reader:
            if all(row):  # This checks if all columns in the row have values
                writer.writerow(row)


# Usage example
filter_csv('concat_index.csv', 'parsed_index.csv')

# Load the filtered CSV file with new column names
df = pd.read_csv('parsed_index.csv', header=0)
df.columns = new_column_names  # Assign new column names

# Save the DataFrame with new headers
df.to_csv('updated_parsed_index.csv', index=False)
print("CSV file has been updated and saved as 'updated_parsed_index.csv'.")