import re
def find_str(string):
    patterns = '^[a-z]+_[a-z]+$'
    if re.search(patterns,  string):
            print(True)
    else:
            print(False)
string = input()
find_str(string)