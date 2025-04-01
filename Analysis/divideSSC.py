import re

def add_blank_lines(content):
    # Define a regex pattern to split questions based on "Q." followed by a number
    pattern = r"(?=Q\.\d+)"
    
    # Split the content by the pattern, keeping the questions intact
    questions = re.split(pattern, content)
    
    # Remove any empty strings from the result
    questions = [q.strip() for q in questions if q.strip()]
    
    # Join the questions with two newlines to add a blank line between each question
    formatted_content = "\n\n".join(questions)
    
    return formatted_content

def process_file(file_path):
    # Read the content from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Process the content to add blank lines between questions
    formatted_content = add_blank_lines(content)
    
    # Overwrite the file with the formatted content
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(formatted_content)

# Example usage
file_path = "D:/Zynx/Notes/Exam/GS/SSC 2024 Prelims GS allShift.txt"  # Replace with the path to your markdown file
process_file(file_path)
