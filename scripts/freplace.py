import os
import re
import sys

def replace_string(old_string, new_string):
    base_dir = os.getcwd()

    for root, dirs, files in os.walk(base_dir):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r') as f:
                    content = f.read()

                new_content = re.sub(old_string, new_string, content)

                if new_content != content:
                    with open(file_path, 'w') as f:
                        f.write(new_content)
                    print "Modified file: %s" % file_path
            except IOError:
                print "Error: Could not read file '%s'" % file_path

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Usage: python script.py old_string new_string"
        sys.exit(1)
    
    old_string = sys.argv[1]
    new_string = sys.argv[2]
    replace_string(old_string, new_string)

