import os
from unstructured.partition.text import partition_text
from unstructured.cleaners.core import group_broken_paragraphs
from unstructured.cleaners.core import new_line_grouper
from unstructured.cleaners.core import group_bullet_paragraph
from unstructured.cleaners.core import blank_line_grouper
from unstructured.cleaners.core import auto_paragraph_grouper
from unstructured.cleaners.core import clean_bullets
from unstructured.chunking.title import chunk_by_title


os.environ["DO_NOT_TRACK"] = "true"
print("processing")
elements = partition_text(filename="Exam/GS/26 years UPSC Prelims.txt", paragraph_grouper=auto_paragraph_grouper)
print("processed")

for element in elements :
    print(str(element)+"\n\n")

# with open("example-docs/fake-text.txt", "r") as f:
#   elements = partition_text(file=f)

# with open("example-docs/fake-text.txt", "r") as f:
#   text = f.read()
# elements = partition_text(text=text)


