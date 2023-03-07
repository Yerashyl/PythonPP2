def is_palindrome(string):
    if string == ''.join(reversed(string)):
        return True
    else: return False

s = input()
if is_palindrome(s):
    print("Yes")
else:
    print("No")