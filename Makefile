.PHONY: all concat parse convert finally year-% re

# Run all steps in order
all: concat parse convert finally

# Concatenate CSV files
concat:
	python functions/concat_csv.py

# Parse the concatenated CSV file
parse:
	python functions/parse_csv.py

# Convert data
convert:
	python functions/convert_hr.py 
	python functions/convert_ac.py 
	python functions/convert_tc.py

# Calculate final score
finally:
	python functions/algorithm.py
# Clean up generated files
clean:
	rm -f /*/*_index.csv
	rm -f *.pyc
	rm -rf __pycache__

year-%:
	python functions/parse_by_year.py $*
	python functions/create_map.py $*

# Rebuild everything
re: clean all