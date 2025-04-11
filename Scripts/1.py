import re

def convert_verse(verse_data):
    """
    Converts a verse string with Greek words and annotations into a simplified format.

    Args:
        verse_data: A string representing the verse data.

    Returns:
        A string with the simplified format.
    """
    parts = verse_data.split(",", 1)
    verse_number = parts[0]
    text_part = parts[1]

    matches = re.findall(r"\[([^\]]+)\](?:\[([^\]#()]+)(?:#[^\]]*)?\])?", text_part)
    output_parts = [verse_number]

    for match in matches:
        greek_word = match[0]
        translation = match[1] if match[1] else ""
        output_parts.append(greek_word)
        if translation:
            output_parts.append(translation.strip())

    return "\t".join(output_parts)

def process_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r', encoding='utf-8') as infile, \
             open(output_filename, 'w', encoding='utf-8') as outfile:
            for line in infile:
                line = line.strip()
                if line:  # Process non-empty lines
                    converted_line = convert_verse(line)
                    outfile.write(converted_line + '\n')
        print(f"Successfully processed '{input_filename}' and wrote to '{output_filename}'.")
    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = "2.csv"  # Replace with your input filename
    output_file = "2.txt"  # Replace with your desired output filename


    process_file(input_file, output_file)