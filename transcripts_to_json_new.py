import os
import json

input_folder = "output_transcripts"
output_file = os.path.join(input_folder, "all_transcripts.ndjson")

files = [f for f in os.listdir(input_folder) if f.endswith(".json")]

with open(output_file, "w", encoding="utf-8") as ndjson_file:
    for filename in files:
        file_path = os.path.join(input_folder, filename)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

                # Remove the "raw_entries" key if it exists
                data.pop("raw_entries", None)

                ndjson_file.write(json.dumps(data, ensure_ascii=False) + "\n")
        except Exception as e:
            print(f"❌ Failed to process {filename}: {e}")

print(f"✅ NDJSON written to: {output_file}")
