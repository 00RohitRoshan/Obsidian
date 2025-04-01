import re

def add_blank_lines(text):
    # Ensure question numbers capture entire question titles and multi-line content
    pattern = re.compile(r"(\n?\s*\d+\.\s.*?(?:\n(?:\s{2,}|[a-dA-D]\)|\[\d{4}\])?.*)*)")

    # Split the text while keeping the questions
    parts = pattern.split(text)

    # Rebuild the text with two blank lines before each question
    formatted_text = "\n\n".join([part.strip() for part in parts if part.strip()]) + "\n"

    return formatted_text

def process_file(file_path):
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Process the content
    formatted_content = add_blank_lines(content)
    
    # Overwrite the file with formatted content
    with open(file_path, 'w', encoding='utf-8', newline='\n') as file:
        file.write(formatted_content)

# Example usage
file_path = "D:/Zynx/Notes/Exam/GS/26 years UPSC Prelims.txt"  # Replace with your actual file path
process_file(file_path)
