import pandas as pd

def convert_to_boolean(file_path, columns):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Iterate over the specified columns and update them
    for column in columns:
        df[column] = (df[column] != 0).astype(int)
    
    # Save the updated DataFrame back to the CSV file
    df.to_csv(file_path, index=False)

# Example usage:
file_path = 'insecurity_index.csv'
columns = ["Armed Conflict Deaths"]
convert_to_boolean(file_path, columns)
