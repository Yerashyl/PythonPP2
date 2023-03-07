def is_true(lol_tuple):
    if all(lol_tuple):
        return True
    else:
        return False
sam_tuple = (1, 2, 3, 4)
print(is_true(sam_tuple))