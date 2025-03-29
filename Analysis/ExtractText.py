import PyPDF2
import os
import re, argparse

def pdf_to_text_pypdf2(pdf_path):
    # Open the PDF file in read-binary mode
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        
        text = ""
        # Loop through all pages in the PDF
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()  # Extract text from each page

    # List of prefixes to remove from the text
    prefixes_to_remove = [
        "Question ID :",
        "Option 1 ID :",
        "Option 2 ID :",
        "Option 3 ID :",
        "Option 4 ID :",
        "Status :",
        "Chosen Option :"
    ]
    
    # Split the text into lines
    lines = text.splitlines()

    # Filter out lines that start with any of the specified prefixes
    filtered_lines = [line for line in lines if not any(line.startswith(prefix) for prefix in prefixes_to_remove)]

    # Add separator based on increasing Q numbers
    separator = "\n--- New Section ---\n"
    sectioned_text = []
    current_section = []

    # Regular expression pattern to detect "Question ID : Q[Number]"
    question_pattern = r"Q.1 "

    for line in filtered_lines:
        # Check if the line matches the "Question ID : Q[number]" pattern
        match = re.match(question_pattern, line)
        if match:
            # If the current section is not empty, append it with a separator
            if current_section:
                sectioned_text.append("\n".join(current_section))
                sectioned_text.append(separator)  # Add the separator
            
            # Start a new section with the current question
            current_section = [line]
        else:
            # Otherwise, add the line to the current section
            current_section.append(line)

    # Add the last section if it exists
    if current_section:
        sectioned_text.append("\n".join(current_section))

    # Join all sections with the separator in between
    final_text = "\n".join(sectioned_text)

    # Get the output file path by changing the extension of the input PDF path
    output_path = os.path.splitext(pdf_path)[0] + ".txt"

    # Write the final text with separators to the output file
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(final_text)

    print(f"Text has been extracted and saved to {output_path}")

# # Example usage
# pdf_path = "20-Jan-Paper-I-EN.pdf"  # Replace with your PDF file path
# pdf_to_text_pypdf2(pdf_path)

# Main function to handle command-line arguments
if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Extract text from a PDF and categorize questions.")
    parser.add_argument('pdf_path', type=str, help="The path to the input PDF file.")
    
    # Parse arguments
    args = parser.parse_args()

    # Run the function with the provided PDF file path
    pdf_to_text_pypdf2(args.pdf_path)
