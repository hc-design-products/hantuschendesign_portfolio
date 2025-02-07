import os
import glob

# Define the directory path
directory_path = '/Users/tonkatsu/Documents/GitHub/hc-design'  # Update this to your directory path

# Get all .html files
html_files = glob.glob(os.path.join(directory_path, '*.html'))

# Function to update the language switcher links in the HTML file
def update_language_switcher(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Determine the base name of the file without the extension
    base_name = os.path.basename(file_path)
    name, ext = os.path.splitext(base_name)

    # Determine the corresponding link for EN and JP
    if '_jp' in name:
        en_link = name.replace('_jp', '') + ext
        jp_link = name + ext
    else:
        en_link = name + ext
        jp_link = name + '_jp' + ext

    # Define the new language switcher HTML content
    new_language_switcher_html = f"""
    <div class="language-switcher-container">
      <div class="language-switcher">
        <a class="language-switcher-not-active" href="{en_link}">EN</a>
        <a class="language-switcher-active" href="{jp_link}">JP</a>
      </div>
    </div>
    """

    # Replace the content between <!-- START LANGUAGE --> and <!-- END LANGUAGE -->
    start_tag = '<!-- START LANGUAGE -->'
    end_tag = '<!-- END LANGUAGE -->'
    start_index = content.find(start_tag)
    end_index = content.find(end_tag) + len(end_tag)

    if start_index != -1 and end_index != -1:
        new_content = content[:start_index + len(start_tag)] + new_language_switcher_html + content[end_index:]

        # Write the updated content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated: {file_path}")

# Update the language switcher in each HTML file
for file_path in html_files:
    update_language_switcher(file_path)

print("Language switcher updated in all applicable HTML files.")