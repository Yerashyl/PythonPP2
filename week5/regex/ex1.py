import re
def find_str(string):
    pattern = re.findall(r'ab*', string)
    if pattern:
        print(True)
    else:
        print(False)
string = input()
find_str(string)