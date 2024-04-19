import pandas as pd

def convert_columns_to_boolean(file_path, columns):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Iterate over the specified columns and update them
    for column in columns:
        df[column] = (df[column] != 0).astype(int)
    
    # Save the updated DataFrame back to the CSV file
    df.to_csv(file_path, index=False)

# Example usage:
file_path = 'updated_rates_echelons.csv'
columns = ["Armed Conflict Deaths", "Homicide Rate"]
convert_columns_to_boolean(file_path, columns)
