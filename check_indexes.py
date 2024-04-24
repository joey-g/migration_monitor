import re
import sys

TABLES_TO_TEST = ['migration_monitor_user']

def check_migration(contents):
    for table in TABLES_TO_TEST:
        # This regular expression matches 'CREATE INDEX' statements for the given table
        # that are not followed by 'CONCURRENTLY'.
        # It uses a negative lookahead assertion to ensure 'CONCURRENTLY' does not follow 'CREATE INDEX'.
        if re.search(r'CREATE INDEX .* ON {} (?!CONCURRENTLY)'.format(table), contents, re.MULTILINE | re.IGNORECASE):
            print('Warning: Migration adds an index without the CONCURRENTLY option on table {}'.format(table))
            print('Migration contents:')
            print(contents)
            sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            contents = file.read()
        check_migration(contents)
    else:
        check_migration(sys.stdin.read())
