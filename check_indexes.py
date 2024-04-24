import re
import sys

TABLES_TO_TEST = ['migration_monitor_user']

def check_migration(contents):
    print('Migration contents:')
    print(contents)
    for table in TABLES_TO_TEST:
        # Regular expression matches 'CREATE INDEX' statements for the given table that are
        # not followed by 'CONCURRENTLY'. oUses a negative lookahead assertion to ensure
        # 'CONCURRENTLY' does not follow 'CREATE INDEX'.
        regex = r'CREATE INDEX .* ON "?{}"? (?!.*CONCURRENTLY)'.format(table)
        if re.search(regex, contents, re.MULTILINE | re.IGNORECASE):
            print('Warning: Migration adds an index without the CONCURRENTLY option on table {}'.format(table))
            sys.exit(1)
        else:
            print('Migration is valid')
            sys.exit(0)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            contents = file.read()
        check_migration(contents)
    else:
        check_migration(sys.stdin.read())
