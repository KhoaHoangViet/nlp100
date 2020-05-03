def interlock(str1, str2):
    if len(str2) > len(str1):
        str1, str2 = str2, str1

    list1, list2 = map(list, [str1, str2])
    for i in range(len(list2)):
        list1.insert(i*2 + 1, list2[i])
    return "".join(list1)
