import pandas as pd
import argparse

def filter_and_save_by_year(Year):
    # Specify the file path directly
    file_path = 'insecurity_index.csv'
    
    # Read the dataset
    df = pd.read_csv(file_path)

    # Filter the dataset for the given year
    df_filtered = df[df['Year'] == Year]

    # Construct the output filename
    output_file = f"{Year}_index.csv"

    # Save the filtered data to a new CSV file
    df_filtered.to_csv(output_file, index=False)
    print(f"Filtered data saved to {output_file}")

def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Filter CSV rows by Year and save to a new file.")
    parser.add_argument('year', type=int, help='The Year to filter by')

    # Parse arguments
    args = parser.parse_args()

    # Call the function with the year from the command line
    filter_and_save_by_year(args.year)

if __name__ == "__main__":
    main()
