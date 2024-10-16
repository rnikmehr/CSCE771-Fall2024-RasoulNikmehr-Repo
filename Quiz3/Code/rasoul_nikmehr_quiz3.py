
!pip install pandas
!pip install nltk
!pip install textblob

import csv
import json
from datetime import datetime

# Function to convert CSV to JSON format
def csv_to_json(csv_file_path, json_file_path, state_abbr, contributor_name):
    # Read the CSV file
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # Create a list to store question-answer pairs
        qa_list = []

        # Loop through each row in the CSV file
        for row in csv_reader:
            qa_list.append({
                "q": row["Question"],  # Adjust column name if necessary
                "a": row["Answer"],    # Adjust column name if necessary
                "s": row["Source"],    # Adjust column name if necessary
                "t": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")  # Current UTC time
            })

        # Prepare the final structure for JSON
        dataset = {
            "state": state_abbr,
            "num_questions": len(qa_list),
            "num_answers": len(qa_list),
            "contributor": contributor_name,
            "questions": qa_list
        }

        # Write the JSON to a file
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(dataset, json_file, indent=4)

        print(f"JSON dataset has been saved to {json_file_path}")

# Define the file paths and other details
csv_file_path = "/content/SC-Election-Data-ClassExercise.xlsx - Sept-2024.csv"
json_file_path = "sc_qa.json"  # Output JSON file
state_abbr = "SC"
contributor_name = "AI4S"

# Convert the CSV to JSON
csv_to_json(csv_file_path, json_file_path, state_abbr, contributor_name)

import csv
import json
from datetime import datetime

# Function to convert CSV to JSON format
def csv_to_json(csv_file_path, json_file_path, state_abbr, contributor_name):
    # Read the CSV file
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row if present

        # Create a list to store question-answer pairs
        qa_list = []

        # Loop through each row in the CSV file
        for row in csv_reader:
            # Check if the row represents a question (Text type) and has data
            if row[0] == "Text" and row[1].strip() != "" and row[2].strip() != "":
                qa_list.append({
                    "q": row[1],  # Question text
                    "a": row[2],  # Answer or source text
                    "s": "https://www.vote411.org/illinois",  # Static source URL based on your dataset
                    "t": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")  # Current UTC time
                })

        # Prepare the final structure for JSON
        dataset = {
            "state": state_abbr,
            "num_questions": len(qa_list),
            "num_answers": len(qa_list),
            "contributor": contributor_name,
            "questions": qa_list
        }

        # Write the JSON to a file
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(dataset, json_file, indent=4)

        print(f"JSON dataset has been saved to {json_file_path}")

# Define the file paths and other details
csv_file_path = "/content/election_data_combined.csv"  # Replace with your actual CSV file path
json_file_path = "il_qa.json"  # Output JSON file
state_abbr = "IL"  # Illinois state abbreviation
contributor_name = "Rasoul Nikmehr"

# Convert the CSV to JSON
csv_to_json(csv_file_path, json_file_path, state_abbr, contributor_name)

