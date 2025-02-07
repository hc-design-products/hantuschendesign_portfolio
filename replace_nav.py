import os
import glob

# Read the content of nav.html
with open('nav.html', 'r', encoding='utf-8') as file:
    nav_content = file.read()

# Extract the content between <nav> and </nav>
start_tag = '<nav'
end_tag = '</nav>'
start_index = nav_content.find(start_tag)
end_index = nav_content.find(end_tag) + len(end_tag)
nav_section = nav_content[start_index:end_index]

# Get all .html files excluding *_jp.html files
html_files = [file for file in glob.glob('*.html') if '_jp.html' not in file]

# Replace the content between <nav> and </nav> in each file
for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Find the existing <nav> section
    start_index = content.find(start_tag)
    end_index = content.find(end_tag) + len(end_tag)
    
    if start_index != -1 and end_index != -1:
        # Replace the existing <nav> section with the new one
        new_content = content[:start_index] + nav_section + content[end_index:]
        
        # Write the updated content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)

print("Replacement complete.")