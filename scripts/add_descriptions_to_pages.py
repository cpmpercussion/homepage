# borrowed from ARJ: https://www.arj.no/2024/07/13/blog-descriptions/
import re
from pathlib import Path

# Define the directory where your blog posts are stored
content_dir = Path('../_posts')

# Function to extract text for the description
def extract_description(text, max_length=155):
    # Remove markdown links/images, HTML tags, markdown headings, and special characters
    clean_text = re.sub(r'!\[.*?\]\(.*?\)|<[^>]+>|\[(.*?)\]\(.*?\)|#+|{%.*?%}|{{.*?}}', r'\1', text)
    clean_text = re.sub(r'[*#_:]+', '', clean_text)  # Keeps only alphanumeric characters and spaces
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()  # Normalize whitespace and strip leading/trailing whitespace
    if len(clean_text) > max_length:
        return clean_text[:max_length].rsplit(' ', 1)[0]
    return clean_text

# Function to update the markdown file by appending the description to the front matter
def update_file_with_description(md_file_path, front_matter, description):
    updated_front_matter = f'---\n{front_matter}\ndescription: "{description}"\n---\n\n'
    main_content = content[front_matter_match.end():].lstrip()
    updated_content = updated_front_matter + main_content
    
    # Write the updated content back to the file
    with open(md_file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)
    print(f'Updated {md_file_path}')

# Iterate through the markdown files in the content directory
for md_file in content_dir.rglob('*.md'):
    print(f'Processing file: {md_file}')
    
    with open(md_file, 'r', encoding='utf-8') as file:
        content = file.read()
        
    front_matter_match = re.search(r'^---\s*(.*?)\s*---', content, re.DOTALL)
    if front_matter_match and 'description:' not in front_matter_match.group(1):
        front_matter = front_matter_match.group(1)
        description = extract_description(content[front_matter_match.end():])
        update_file_with_description(md_file, front_matter, description)
    else:
        print(f'No update required or front matter not found in {md_file}')
