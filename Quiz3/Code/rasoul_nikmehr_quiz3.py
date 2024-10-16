
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
csv_file_path = "/content/SC-Election-Data-ClassExercise.xlsx - Sept-2024.csv"  # Replace with your actual CSV file path
json_file_path = "sc_qa.json"  # Output JSON file
state_abbr = "SC"
contributor_name = "AI4S"  # Replace with your actual name

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

import json

# Load South Carolina dataset
with open('sc_qa.json', 'r') as sc_file:
    sc_data = json.load(sc_file)
    sc_questions = sc_data['questions']

# Load Illinois dataset
with open('il_qa.json', 'r') as il_file:
    il_data = json.load(il_file)
    il_questions = il_data['questions']
# Lexical diversity calculation function
def lexical_diversity(text):
    words = text.split()
    return len(set(words)) / len(words) if words else 0

# Average lexical diversity function
def avg_lexical_diversity(entries, key="q"):  # "q" for questions, "a" for answers
    diversities = [lexical_diversity(entry[key]) for entry in entries]
    return sum(diversities) / len(diversities) if diversities else 0

# Average response length (word count) function
def avg_response_length(entries, key="q"):  # "q" for questions, "a" for answers
    lengths = [len(entry[key].split()) for entry in entries]  # Word count
    return sum(lengths) / len(lengths) if lengths else 0

# South Carolina dataset comparisons (Questions)
sc_lexical_diversity = avg_lexical_diversity(sc_questions, key="q")
sc_question_length = avg_response_length(sc_questions, key="q")

# Illinois dataset comparisons (Questions)
il_lexical_diversity = avg_lexical_diversity(il_questions, key="q")
il_question_length = avg_response_length(il_questions, key="q")

# Output the comparison for questions
print(f"SC Lexical Diversity (Questions): {sc_lexical_diversity}, IL Lexical Diversity (Questions): {il_lexical_diversity}")
print(f"SC Average Question Length: {sc_question_length} words, IL Average Question Length: {il_question_length} words")

# South Carolina dataset comparisons (Answers)
sc_lexical_diversity_answers = avg_lexical_diversity(sc_questions, key="a")
sc_answer_length = avg_response_length(sc_questions, key="a")

# Illinois dataset comparisons (Answers)
il_lexical_diversity_answers = avg_lexical_diversity(il_questions, key="a")
il_answer_length = avg_response_length(il_questions, key="a")

# Output the comparison for answers
print(f"SC Lexical Diversity (Answers): {sc_lexical_diversity_answers}, IL Lexical Diversity (Answers): {il_lexical_diversity_answers}")
print(f"SC Average Answer Length: {sc_answer_length} words, IL Average Answer Length: {il_answer_length} words")

# Function to compare answer vs. question based on lexical diversity and length
def compare_q_a(entries):
    lexical_diversity_diff = []
    length_diff = []

    for entry in entries:
        q_lexical = lexical_diversity(entry["q"])
        a_lexical = lexical_diversity(entry["a"])
        lexical_diversity_diff.append(a_lexical - q_lexical)

        q_length = len(entry["q"].split())
        a_length = len(entry["a"].split())
        length_diff.append(a_length - q_length)

    avg_lexical_diff = sum(lexical_diversity_diff) / len(lexical_diversity_diff) if lexical_diversity_diff else 0
    avg_length_diff = sum(length_diff) / len(length_diff) if length_diff else 0

    return avg_lexical_diff, avg_length_diff

# South Carolina question vs. answer comparison
sc_lexical_diff, sc_length_diff = compare_q_a(sc_questions)

# Illinois question vs. answer comparison
il_lexical_diff, il_length_diff = compare_q_a(il_questions)

# Output the comparison for question-answer pairs
print(f"SC Avg Lexical Difference (Answer - Question): {sc_lexical_diff}, IL Avg Lexical Difference: {il_lexical_diff}")
print(f"SC Avg Length Difference (Answer - Question): {sc_length_diff} words, IL Avg Length Difference: {il_length_diff} words")

