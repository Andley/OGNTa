# Read input file and process its contents
def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            # Split the line into segments
            segments = line.strip().split("\t")
            ref = segments[0]  # Reference (e.g., 1:1, 1:2, etc.)
            
            # Iterate over the segments two at a time (starting after the reference)
            for i in range(1, len(segments), 2):
                if i + 1 < len(segments):  # Check to avoid index errors
                    # Write the reformatted row to the output file
                    # print(f"{ref}\t{segments[i]}\t{segments[i+1]}\n")
                    outfile.write(f"{ref}\t{segments[i]}\t{segments[i+1]}\n")

# Specify input and output file names
input_file = "27-啟示錄.tsv"  # Replace with your input file name
output_file = "27-啟示錄.txt"  # Replace with your desired output file name

# Process the input file
process_file(input_file, output_file)

print(f"File processed successfully. Output saved to {output_file}.")
