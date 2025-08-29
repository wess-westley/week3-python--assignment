# Python script to process a text file

def process_file():
    try:
        # Step 1: Read contents of input.txt
        with open("input.txt", "r", encoding="utf-8") as file:
            text = file.read()

        # Step 2: Count number of words
        word_count = len(text.split())

        # Step 3: Convert all text to uppercase
        processed_text = text.upper()

        # Step 4: Write processed text + word count to output.txt
        with open("output.txt", "w", encoding="utf-8") as file:
            file.write("Processed Text:\n")
            file.write(processed_text + "\n\n")
            file.write(f"Word Count: {word_count}\n")

        # Step 5: Print success message
        print("✅ Success! File 'output.txt' has been created.")

    except FileNotFoundError:
        print("❌ Error: 'input.txt' not found. Please create it first.")

# Run the function
process_file()
