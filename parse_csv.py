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
