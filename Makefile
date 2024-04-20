.PHONY: all concat parse convert finally year-% re

# Run all steps in order
all: concat parse convert finally

# Concatenate CSV files
concat:
	python concat_csv.py

# Parse the concatenated CSV file
parse:
	python parse_csv.py

# Convert data
convert:
	python convert_hr.py 
	python convert_ac.py 
	python convert_tc.py

# Calculate final score
finally:
	python algorithm.py
# Clean up generated files
clean:
	rm -f *_index.csv
	rm -f *.pyc
	rm -rf __pycache__

year-%:
	python parse_by_year.py $*

# Rebuild everything
re: clean all