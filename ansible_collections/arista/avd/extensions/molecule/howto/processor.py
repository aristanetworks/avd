import sys
import yaml
import os

# Define the output directory constant
OUTPUT_DIR = "docs_artifacts"

def load_file(filepath):
    if not os.path.exists(filepath):
        print(f"ERROR: File not found: {filepath}")
        return None
    with open(filepath, 'r') as f:
        return f.read().splitlines()

def extract_section(lines, section_header):
    buffer = []
    capture = False

    for line in lines:
        stripped = line.strip()

        # 1. Check start of section
        if line.startswith(section_header) and not capture:
            capture = True
            buffer.append(line)
            continue

        # 2. Capture logic
        if capture:
            if not stripped:
                continue

            indent_level = len(line) - len(line.lstrip())

            # Stop if we hit a non-indented line that is NOT a comment
            if indent_level == 0 and not line.startswith("!"):
                break

            buffer.append(line)

    return buffer

def process_config(config_path):
    print(f"--- Loading Job Config: {config_path} ---")

    # Ensure output directory exists
    if not os.path.exists(OUTPUT_DIR):
        try:
            os.makedirs(OUTPUT_DIR)
            print(f"Created directory: {OUTPUT_DIR}")
        except OSError as e:
            print(f"Error creating directory {OUTPUT_DIR}: {e}")
            sys.exit(1)

    with open(config_path, 'r') as f:
        jobs = yaml.safe_load(f)

    for job in jobs:
        target_file = job.get('file')
        sections_to_find = job.get('sections', [])
        artifact_filename = job.get('artifact')

        # Combine directory and filename
        full_output_path = os.path.join(OUTPUT_DIR, artifact_filename)

        print(f"Processing target: {target_file}")

        eos_lines = load_file(target_file)
        if not eos_lines:
            continue

        extracted_data = []

        for header in sections_to_find:
            print(f"  > Searching for section: '{header}'")
            block = extract_section(eos_lines, header)

            if block:
                # Clean up trailing '!'s
                while block and block[-1].strip() == "!":
                    block.pop()

                extracted_data.extend(block)
                # Add exactly one separator after the clean block
                extracted_data.append("!")
            else:
                print(f"  > WARNING: Section '{header}' not found.")

        if extracted_data:
            with open(full_output_path, 'w') as out:
                out.write("\n".join(extracted_data))
            print(f"  > Success: Data written to {full_output_path}\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 processor.py <path_to_config.yml>")
        sys.exit(1)

    process_config(sys.argv[1])
