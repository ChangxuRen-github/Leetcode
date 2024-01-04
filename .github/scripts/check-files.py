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
                    links.append((match.group(1), match.group(2)))
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
            if match:
                file_date = datetime.datetime.strptime(match.group(1), '%Y-%m-%d %H:%M:%S').date()
                today = datetime.date.today()
                # Check if the date is 1, 3, or 15 days ago
                return file_date in [today - datetime.timedelta(days=d) for d in [1, 3, 15]]
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
    return False

def main():
    # Path to the Leetcode/Questions directory in the repository
    base_path = 'Leetcode/Questions'  # Modify this path if different
    repo = Repo('.')
    recent_links = []

    # Check each file in the Leetcode/Questions directory
    for file in repo.git.ls_tree('-r', '--name-only', 'HEAD', base_path).splitlines():
        file_path = os.path.join(base_path, file)
        if is_recent_file(file_path):
            links = extract_leetcode_links(file_path)
            recent_links.extend(links)

    # Output the links to check
    with open('links_to_check.txt', 'w') as f:
        for name, url in recent_links:
            f.write(f"{name}: {url}\n")

if __name__ == "__main__":
    main()
