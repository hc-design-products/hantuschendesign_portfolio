import os

# Directory containing the HTML files
directory = '/Users/tonkatsu/Documents/GitHub/hantuschendesign/'

# Poppins font link to be added
poppins_link = '''<link
      href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap"
      rel="stylesheet"
    />'''

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        
        # Read the file content
        with open(filepath, 'r') as file:
            content = file.read()
        
        # Add the Poppins font link before the Vendor CSS Files comment
        content = content.replace('<!-- Vendor CSS Files -->', f'{poppins_link}\n    <!-- Vendor CSS Files -->')
        
        # Write the updated content back to the file
        with open(filepath, 'w') as file:
            file.write(content)

print("Poppins font link added to all HTML files successfully.")