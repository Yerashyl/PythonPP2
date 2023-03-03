import re
def find_str(string):
    string = re.sub("[ ,.]", ':', string)
    print(string)
string = input()
find_str(string)