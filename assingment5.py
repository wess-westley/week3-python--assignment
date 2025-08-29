# file_read_write.py

def read_and_modify(input_file, output_file):
    try:
        with open(input_file, "r") as infile:
            content = infile.read()
        
        # Modify content (example: uppercase)
        modified_content = content.upper()

        with open(output_file, "w") as outfile:
            outfile.write(modified_content)

        print(f"✅ File '{input_file}' read successfully and written to '{output_file}'")

    except FileNotFoundError:
        print(f"❌ Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")


# Example usage
read_and_modify("input.txt", "output.txt")
