import re
def find_str(string):
    string = re.split("[A-Z]", string)
    print(string)
string = input()
find_str(string)