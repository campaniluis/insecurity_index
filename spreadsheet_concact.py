import pandas as pd

df1 = pd.read_csv('./murder_rate_index_EPS.csv')
df2 = pd.read_csv('./armed_conflict_deaths_index_EPS.csv')
df3 = pd.read_csv('./territorial_crl_index_EPS.csv')

merged_df = df1.merge(df2, on=['Entity', 'Code', 'Year'], how='outer').merge(df3, on=['Entity', 'Code', 'Year'], how='outer')


merged_df.to_csv('./final_index.csv', index=False)
