import re
def find_str(string):
    patterns = 'a*+b$'
    if re.search(patterns,  string):
            print(True)
    else:
            print(False)
string = input()
find_str(string)