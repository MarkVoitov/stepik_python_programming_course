def modify_list(lst):
    for i in lst[::-1]:
        if i % 2 != 0:
            lst.remove(i)
    for i in range(len(lst)):
        lst[i] = lst[i] // 2