import pandas as pd

df1 = pd.read_csv('updated_homicide-rate-echelons.csv')
df2 = pd.read_csv('death-rate-in-armed-conflicts.csv')
df3 = pd.read_csv('percentage-of-territory-controlled-by-government.csv')


#  'Entity' and 'Year'
countries1 = set(df1['Entity'])
times1 = set(df1['Year'])

countries2 = set(df2['Entity'])
times2 = set(df2['Year'])

countries3 = set(df3['Entity'])
times3 = set(df3['Year'])

# Find common countries and times
common_countries = countries1.intersection(countries2, countries3)
common_times = times1.intersection(times2, times3)


# Optional: Filter original DataFrames to keep only rows with common countries and times
filtered_df1 = df1[df1['Entity'].isin(common_countries) & df1['Year'].isin(common_times)]
filtered_df2 = df2[df2['Entity'].isin(common_countries) & df2['Year'].isin(common_times)]
filtered_df3 = df3[df3['Entity'].isin(common_countries) & df3['Year'].isin(common_times)]

# Now, filtered_df1, filtered_df2, and filtered_df3 contain only the common countries and times
# Save the filtered DataFrames to new CSV files
filtered_df1.to_csv('filtered_spreadsheet1.csv', index=False)
filtered_df2.to_csv('filtered_spreadsheet2.csv', index=False)
filtered_df3.to_csv('filtered_spreadsheet3.csv', index=False)
