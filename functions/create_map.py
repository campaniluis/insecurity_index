import sys
import pygal
import csv
from pygal.maps.world import World

def generate_map_for_year(csv_filename):
    # Open the CSV file for the specified year
    with open(csv_filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        
        # Find the index for 'Country Code' and 'Score'
        code_idx = header_row.index('ISO Code')
        score_idx = header_row.index('Score')
        
        # Prepare data for the map
        cc_data = {}
        for row in reader:
            country_code = row[code_idx]
            data_value = float(row[score_idx])
            if country_code:
                cc_data[country_code] = data_value
        
        # Generate the map
        wm = World()
        year = csv_filename.split("_")[-1].split(".")[0]
        wm.title = f'Global Data Visualization for {year}'
        wm.add('Data', cc_data)
        wm.render_to_file(f'output_data/{year}_index.svg')

if __name__ == "__main__":
    # Get the year from command line arguments
    year = sys.argv[1]
    csv_filename = f'output_data/{year}_index.csv'
    generate_map_for_year(csv_filename)
