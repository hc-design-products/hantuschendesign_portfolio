import os
import glob

# Define the language switcher HTML content
language_switcher_html = """
<!-- START LANGUAGE -->
<div class="language-switcher-container">
  <div class="language-switcher">
    <a class="language-switcher-active" href="index.html">EN</a>
    <a class="language-switcher-not-active" href="index_jp.html">JP</a>
  </div>
</div>
<!-- END LANGUAGE -->
"""

# Define the directory path
directory_path = '/Users/tonkatsu/Documents/GitHub/hc-design'  # Update this to your directory path

# Get all .html files excluding *_jp.html files
html_files = [file for file in glob.glob(os.path.join(directory_path, '*.html')) if '_jp.html' not in file]

# Function to add the language switcher to the specified place in the HTML file
def add_language_switcher(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Define the place where you want to insert the language switcher
    insert_after = '<div id="colorlib-page">'

    if insert_after in content:
        # Insert the language switcher HTML content
        new_content = content.replace(insert_after, insert_after + language_switcher_html)

        # Write the updated content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated: {file_path}")

# Add the language switcher to each HTML file
for file_path in html_files:
    add_language_switcher(file_path)

print("Language switcher added to all applicable HTML files.")