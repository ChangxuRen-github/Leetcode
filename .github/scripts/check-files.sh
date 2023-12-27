#!/bin/bash

# Function to check if a file was created 1, 3, or 15 days ago
check_file_dates() {
    file_date=$(date -r "$1" +%Y-%m-%d)
    days_ago_1=$(date -d "1 day ago" +%Y-%m-%d)
    days_ago_3=$(date -d "3 days ago" +%Y-%m-%d)
    days_ago_15=$(date -d "15 days ago" +%Y-%m-%d)

    if [[ "$file_date" == "$days_ago_1" || "$file_date" == "$days_ago_3" || "$file_date" == "$days_ago_15" ]]; then
        echo "$1"
    fi
}

# Check each file in the repository
for file in $(git ls-tree -r --name-only HEAD); do
    check_file_dates "$file"
done
