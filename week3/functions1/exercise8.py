def spy_game(lst):
    for i in range(len(lst)):
        if(lst[i]==0):
            for j in range(i, len(lst)-1):
                if lst[j]==0:
                    for g in range(j, len(lst)):
                        if lst[g]==7:
                            return True
    return False