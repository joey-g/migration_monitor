import re
import sys

def check_migration(filename):
    with open(filename, 'r') as file:
        contents = file.read()

    # This regular expression matches 'CREATE INDEX' statements that are not followed by 'CONCURRENTLY'.
    # It uses a negative lookahead assertion to ensure 'CONCURRENTLY' does not follow 'CREATE INDEX'.
    if re.search(r'CREATE INDEX (?!CONCURRENTLY)', contents, re.MULTILINE | re.IGNORECASE):
        print(f'Warning: {filename} adds an index without the concurrently option.')
        sys.exit(1)

if __name__ == '__main__':
    check_migration(sys.argv[1])
