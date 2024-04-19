import numpy as np
import pandas as pd

data = pd.read_csv("insecurity_index.csv")

columns_to_process = [
    "Homicide Rate",
]

# General function to calculate log and apply echelons based on percentiles
def apply_echelon(data, column_name):
    # Ensure the column is numeric, converting non-numeric values to NaN
    data[column_name] = pd.to_numeric(data[column_name], errors='coerce')

    # Compute log for each column, avoiding log(0)
    log_column = np.log(data[column_name] + 1)

    # Calculate percentiles and determine thresholds
    percentiles = [20, 40, 60, 80, 100]
    thresholds = np.percentile(log_column.dropna(), percentiles)

    # Function to determine echelon based on log rate
    def determine_echelon(log_rate):
        for i, threshold in enumerate(thresholds):
            if log_rate <= threshold:
                return str(i + 1)
        return '5'

    # Apply the function to determine echelons for the column
    echelon_values = log_column.apply(determine_echelon)
    data[column_name] = echelon_values  # Update the original column with echelon values

# Apply echelon function to each specified column
for column in columns_to_process:
    apply_echelon(data, column)

# Save the updated spreadsheet
data.to_csv("insecurity_index.csv", index=False)
