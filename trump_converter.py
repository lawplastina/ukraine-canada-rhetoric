import json

input_file = "trump_truth_fuller.json"
output_file = "trump_truth_cleaned.json"

# Open the input file with UTF-16 encoding and read line by line
with open(input_file, "r", encoding="utf-16") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    for line in infile:
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
            # Remove unwanted keys
            obj.pop("account", None)
            obj.pop("media_attachments", None)
            # Write cleaned object as one line in the output
            json.dump(obj, outfile)
            outfile.write("\n")
        except json.JSONDecodeError as e:
            print(f"Skipping line due to JSON error: {e}")
