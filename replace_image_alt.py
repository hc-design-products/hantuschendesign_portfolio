# filepath: /Users/tonkatsu/Documents/GitHub/hc-design/replace_image_alt.py
import os
import glob
import re

# Define the directory path
directory_path = '/Users/tonkatsu/Documents/GitHub/hc-design'  # Update this to your directory path

# Get all .html files
html_files = glob.glob(os.path.join(directory_path, '*.html'))

# Function to remove empty class attributes and update img alt attributes in the HTML file
def update_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Use regex to find and remove empty class attributes
    content = re.sub(r'\sclass=""', '', content)

    # Use regex to remove all alt attributes from img tags
    content = re.sub(r'\s*alt="[^"]*"', '', content)

    # Use regex to add alt="image" to all img tags
    content = re.sub(r'<img([^>]*?)>', r'<img\1 alt="image">', content)

    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Updated: {file_path}")

# Update each HTML file
for file_path in html_files:
    update_html(file_path)

print("Empty class attributes removed and img alt attributes updated in all applicable HTML files.")