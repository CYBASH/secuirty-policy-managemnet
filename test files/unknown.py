import sqlite3
import re

# Function to parse policies from file
def parse_policies(file_path):
    policies = []
    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(r"^(.*?): (.*?) \((v\d+)\)$", line.strip())
            if match:
                name, description, version = match.groups()
                version = int(version[1:])
                policies.append((name, description, version))
    return policies

print(parse_policies("policies.txt"))