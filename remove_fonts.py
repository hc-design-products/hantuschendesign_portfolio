import os
import re

# Directory containing the HTML files
directory = '/Users/tonkatsu/Documents/GitHub/hantuschendesign/'

# Regular expression to match any font link
font_link_pattern = re.compile(r'<link[^>]*href="https://fonts.googleapis.com[^>]*>', re.IGNORECASE)

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        
        # Read the file content
        with open(filepath, 'r') as file:
            content = file.read()
        
        # Remove any font link
        content = re.sub(font_link_pattern, '', content)
        
        # Write the updated content back to the file
        with open(filepath, 'w') as file:
            file.write(content)

print("All font links removed successfully.")