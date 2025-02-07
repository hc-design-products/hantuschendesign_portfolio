import os
import glob
import re

# Define the directory path
directory_path = '/Users/tonkatsu/Documents/GitHub/hc-design'  # Update this to your directory path

# Get all .html files
html_files = glob.glob(os.path.join(directory_path, '*.html'))

# Function to remove slashes before alt attributes in the HTML file
def remove_slash_before_alt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Use regex to find and remove slashes before alt attributes
    content = re.sub(r'/\s*alt=', ' alt=', content)

    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Updated: {file_path}")

# Update each HTML file
for file_path in html_files:
    remove_slash_before_alt(file_path)

print("Slashes before alt attributes removed in all applicable HTML files.")