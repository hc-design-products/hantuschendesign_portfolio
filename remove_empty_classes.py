import os
import glob
import re

# Define the directory path
directory_path = '/Users/tonkatsu/Documents/GitHub/hc-design'  # Update this to your directory path

# Get all .html files
html_files = glob.glob(os.path.join(directory_path, '*.html'))

# Function to remove empty class attributes in the HTML file
def remove_empty_classes(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Use regex to find and remove empty class attributes
    new_content = re.sub(r'\sclass=""', '', content)

    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)
    print(f"Updated: {file_path}")

# Remove empty class attributes in each HTML file
for file_path in html_files:
    remove_empty_classes(file_path)

print("Empty class attributes removed in all applicable HTML files.")