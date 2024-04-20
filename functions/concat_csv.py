import pandas as pd

df1 = pd.read_csv('input_data/death-rate-in-armed-conflicts.csv')
df2 = pd.read_csv('input_data/homicide-rate-unodc.csv')
df3 = pd.read_csv('input_data/percentage-of-territory-controlled-by-government.csv')

merged_df = df1.merge(df2, on=['Entity', 'Code', 'Year'], how='outer').merge(df3, on=['Entity', 'Code', 'Year'], how='outer')


merged_df.to_csv('output_data/insecurity_index.csv', index=False)
