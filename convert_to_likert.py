import numpy as np
import pandas as pd

data = pd.read_csv("updated_parsed_index.csv")

columns_to_process = [
    "Armed Conflict Deaths",
    "Homicide Rate", 
    "Territorial Control",
    "TC Upper Est.",
    "TC Lower Est."
]

# Calculate the logarithm of the homicide rates
#data['Log_Homicide_Rate'] = np.log(data['Homicide rate per 100,000 population - Both sexes - All ages'])

# Creating Likert Scale system based on the log of variables (example uses broad ranges for simplicity)
#echelon_ranges = {
#    '1': (0, np.log(2)),
#    '2': (np.log(2), np.log(5)),
#    '3': (np.log(5), np.log(10)),
#    '4': (np.log(10), np.log(20)),
#    '5': (np.log(20), data['Log_Homicide_Rate'].max() + 1)  # Adding 1 to ensure max value is included
# }

# Function to determine echelon based on log homicide rate
#def determine_echelon(log_rate):
#    for echelon, (lower_bound, upper_bound) in echelon_ranges.items():
#        if lower_bound <= log_rate < upper_bound:
#            return echelon
#    return '1'

# Apply the function to determine echelons
#data['Echelon'] = data['Log_Homicide_Rate'].apply(determine_echelon)

# Select only the necessary columns to simplify the spreadsheet
#data_final = data[['Entity', 'Code', 'Year', 'Echelon']]

# Saving the updated spreadsheet
#output_path = './updated_homicide-rate-echelons.csv'
#data_final.to_csv(output_path, index=False)

#output_path



# List of columns to process

# General function to calculate log and apply echelons based on percentiles
def apply_echelon(data, column_name):
    data[f'Log_{column_name}'] = np.log(data[column_name] + 1)  # Compute log for each column, avoiding log(0)

    # Calculate percentiles and determine thresholds
    percentiles = [20, 40, 60, 80, 100]
    thresholds = np.percentile(data[f'Log_{column_name}'].dropna(), percentiles)

    # Function to determine echelon based on log rate
    def determine_echelon(log_rate):
        for i, threshold in enumerate(thresholds):
            if log_rate <= threshold:
                return str(i + 1)
        return '5'

    # Apply the function to determine echelons for the column
    data[f'Echelon_{column_name}'] = data[f'Log_{column_name}'].apply(determine_echelon)

# Apply echelon function to each specified column
for column in columns_to_process:
    apply_echelon(data, column)

# Select only the necessary columns to simplify the output
columns_to_include = ['Country', 'ISO Code', 'Year']
columns_to_include.extend([f'Echelon_{col}' for col in columns_to_process])
data_final = data[columns_to_include]

# Save the updated spreadsheet
output_path = './updated_rates_echelons.csv'
data_final.to_csv(output_path, index=False)

output_path
