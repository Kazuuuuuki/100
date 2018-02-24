with open("hightemp.txt", "r") as f:
    lines = f.readlines()
    str1 = ""
    for i in range(len(lines)):
        str1 = str1+lines[i][0]
    set1 = set(str1)
    str2 = ""
    for s in set1:
        str2 = str2 + s

    print(str2)
