
import os
import re
import sys

def rename_files(old_pattern, new_pattern):
    base_dir = os.getcwd()

    for root, dirs, files in os.walk(base_dir):
        for file in files:
            old_path = os.path.join(root, file)
            new_file = re.sub(old_pattern, new_pattern, file)
            new_path = os.path.join(root, new_file)

            if old_path != new_path:
                try:
                    os.rename(old_path, new_path)
                    print "Renamed '%s' to '%s'" % (old_path, new_path)
                except Exception as e:
                    print "Error renaming '%s': %s" % (old_path, e)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Usage: python script.py old_pattern new_pattern"
        sys.exit(1)

    old_pattern = sys.argv[1]
    new_pattern = sys.argv[2]
    rename_files(old_pattern, new_pattern)
