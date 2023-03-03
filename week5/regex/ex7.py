import re
def find_str(string):
    print(''.join(x.capitalize() or '_' for x in string.split('_')))
string = input()
find_str(string)