import os
import re
import datetime
from git import Repo

def extract_leetcode_links(file_path):
    links = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Search for Markdown links
                match = re.search(r'\[(.+?)\]\((https://leetcode.com/problems/.+?)\)', line)
                if match:
                    link_text = match.group(1)
                    link_url = match.group(2)
                    # Format the link as Markdown
                    # markdown_link = f"[{link_text}]({link_url})"
                    markdown_link = f"<a href={link_url}>{link_text}</a>"
                    links.append(markdown_link)
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
    return links

def is_recent_file(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read the first line of the file
            first_line = file.readline()
            # Extract timestamp from the HTML comment
            match = re.search(r'<!-- (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) -->', first_line)
            print(file_path)
            if match:
                file_date = datetime.datetime.strptime(match.group(1), '%Y-%m-%d %H:%M:%S').date()
                today = datetime.date.today()
                print(file_date)
                print(today)
                # Check if the date is 1, 3, or 15 days ago
                return file_date in [today - datetime.timedelta(days=d) for d in [1, 3, 15]]
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
    return False

def main():
    print("Chanxu: run main")
    # Path to the Questions directory in the repository
    base_path = './Questions'  # Modify this path if different
    repo = Repo('.')
    recent_links = []

    # Check each file in the Leetcode/Questions directory
    for file in repo.git.ls_tree('-r', '--name-only', 'HEAD', base_path).splitlines():
        file_path = os.path.join('.', file)
        if is_recent_file(file_path):
            links = extract_leetcode_links(file_path)
            recent_links.extend(links)

    # Output the links to check
    with open('links_to_check.txt', 'w') as f:
        for markdown_link in recent_links:
            f.write(f"{markdown_link}\n")
    #debug
    print(recent_links)
if __name__ == "__main__":
    main()
