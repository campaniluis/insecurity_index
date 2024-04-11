import pandas as pd

df1 = pd.read_csv('./death-rate-in-armed-conflicts.csv')
df2 = pd.read_csv('./updated_homicide-rate-echelons.csv')
df3 = pd.read_csv('./percentage-of-territory-controlled-by-government.csv')

merged_df = df1.merge(df2, on=['Entity', 'Code', 'Year'], how='outer').merge(df3, on=['Entity', 'Code', 'Year'], how='outer')


merged_df.to_csv('./concat_index.csv', index=False)