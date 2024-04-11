import numpy as np

import pandas as pd

data = pd.read_csv("concat_index.csv")
# Calculate the logarithm of the homicide rates
data['Log_Homicide_Rate'] = np.log(data['Homicide rate per 100,000 population - Both sexes - All ages'])

# Creating Likert Scale system based on the log of variables (example uses broad ranges for simplicity)
echelon_ranges = {
    '1': (0, np.log(2)),
    '2': (np.log(2), np.log(5)),
    '3': (np.log(5), np.log(10)),
    '4': (np.log(10), np.log(20)),
    '5': (np.log(20), data['Log_Homicide_Rate'].max() + 1)  # Adding 1 to ensure max value is included
}

# Function to determine echelon based on log homicide rate
def determine_echelon(log_rate):
    for echelon, (lower_bound, upper_bound) in echelon_ranges.items():
        if lower_bound <= log_rate < upper_bound:
            return echelon
    return '1'

# Apply the function to determine echelons
data['Echelon'] = data['Log_Homicide_Rate'].apply(determine_echelon)

# Select only the necessary columns to simplify the spreadsheet
data_final = data[['Entity', 'Code', 'Year', 'Echelon']]

# Saving the updated spreadsheet
output_path = './updated_homicide-rate-echelons.csv'
data_final.to_csv(output_path, index=False)

output_path
