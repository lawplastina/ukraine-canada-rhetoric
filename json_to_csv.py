import json
import csv
import pandas as pd

# Input and output file paths
input_file = "trump_truth_fuller.json"
output_file = "trump_truth_fuller.csv"
        
# df = pd.read_json("trump_truth_full.json")
# df.to_csv("trump_truth_full.csv", index=False)

# Pick fields you want in the CSV
fields = ["id", "created_at", "in_reply_to_id", "quote_id",
          "in_reply_to_account_id", "url", "content"]

with open(input_file, 'r', encoding='utf-16') as f_in, \
     open(output_file, 'w', newline='', encoding='utf-8-sig') as f_out:

    writer = csv.DictWriter(f_out, fieldnames=fields)
    writer.writeheader()

    for line in f_in:
        line = line.strip()
        if not line:
            continue  # skip empty lines
        try:
            post = json.loads(line)
            writer.writerow({k: post.get(k, '') for k in fields})
        except json.JSONDecodeError as e:
            print(f"Skipping malformed line: {e}")

# with open(input_file, 'r', encoding='utf-16') as f_in, \
#      open(output_file, 'w', newline='', encoding='utf-8') as f_out:
# 
#     writer = csv.DictWriter(f_out, fieldnames=fields)
#     writer.writeheader()
# 
#     for line_number, line in enumerate(f_in, start=1):
#         line = line.strip()
#         if not line:
#             continue  # skip empty lines
#         try:
#             post = json.loads(line)
#             writer.writerow({k: post.get(k, '') for k in fields})
#         except json.JSONDecodeError as e:
#             print(f"Skipping malformed line {line_number}: {e}")
