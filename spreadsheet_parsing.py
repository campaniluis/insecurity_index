import pandas as pd

df1 = pd.read_csv('updated_homicide-rate-echelons.csv')
df2 = pd.read_csv('death-rate-in-armed-conflicts.csv')
df3 = pd.read_csv('percentage-of-territory-controlled-by-government.csv')


countries1 = set(df1['Entity'])
times1 = set(df1['Year'])

countries2 = set(df2['Entity'])
times2 = set(df2['Year'])

countries3 = set(df3['Entity'])
times3 = set(df3['Year'])

common_countries = countries1.intersection(countries2, countries3)
common_times = times1.intersection(times2, times3)


filtered_df1 = df1[df1['Entity'].isin(common_countries) & df1['Year'].isin(common_times)]
filtered_df2 = df2[df2['Entity'].isin(common_countries) & df2['Year'].isin(common_times)]
filtered_df3 = df3[df3['Entity'].isin(common_countries) & df3['Year'].isin(common_times)]

filtered_df1.to_csv('murder_rate_index_EPS.csv', index=False)
filtered_df2.to_csv('armed_conflict_deaths_index_EPS.csv', index=False)
filtered_df3.to_csv('territorial_crl_index_EPS.csv', index=False)

# Concat
# combined_df = pd.concat([filtered_df1.csv, filtered_df2.csv, filtered_df3.csv], ignore_index=True)

# combined_df.to_csv('security_index_spreadsheet.csv', index=False)
