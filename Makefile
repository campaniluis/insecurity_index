.PHONY: all concat parse likert

# Run all steps in order
all: concat parse likert

# Concatenate CSV files
concat:
	python concat_csv.py

# Parse the concatenated CSV file
parse:
	python parse_csv.py

# Convert data to Likert scale
likert:
	python convert_to_likert.py

# Clean up generated files
clean:
	rm -f concat_index.csv parsed_index.csv updated_parsed_index.csv updated_rates_echelons.csv updated_parsed_index.csv updated_rates_echelons.csv
	rm -f *.pyc
	rm -rf __pycache__

# Rebuild everything
re: clean all