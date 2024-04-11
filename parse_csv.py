import pandas as pd

#df1 = pd.read_csv('concact_index.csv')

#countries1 = set(df1['Death rate in ongoing conflicts in a country (best estimate) - Conflict type: all'])
#times1 = set(df1['Echelon'])
#tctrl = set(df1['terr_contr_vdem_owid'])



#filtered_df1 = df1[df1['Entity'].isin(common_countries) & df1['Year'].isin(common_times)]

#filtered_df1.to_csv('murder_rate_index_EPS.csv', index=False)
#filtered_df2.to_csv('armed_conflict_deaths_index_EPS.csv', index=False)
#filtered_df3.to_csv('territorial_crl_index_EPS.csv', index=False)



import csv

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

