import pandas as pd

def convert_to_boolean(file_path, columns):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Iterate over the specified columns and update them
    for column in columns:
        if column in df.columns:  # Check if the column exists in the DataFrame
            # Convert column to integer, handling non-numeric values
            df[column] = pd.to_numeric(df[column], errors='coerce')
            # Replace NaN values by assigning the result back to the column
            df[column] = df[column].fillna(0)
            # Apply the lambda function to convert values
            df[column] = df[column].apply(lambda x: 1 if x < 95 else 0)
    
    # Save the updated DataFrame back to the CSV file
    df.to_csv(file_path, index=False)

# Example usage:
file_path = 'insecurity_index.csv'
columns = ['Territorial Control', 'TC Upper Est.', 'TC Lower Est.']  # Corrected list of columns
convert_to_boolean(file_path, columns)
