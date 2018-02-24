with open("col1.txt", "r") as f1:
    with open("col2.txt", "r") as f2:
        with open("col.txt", "x") as f:
            lines1 = f1.readlines()
            lines2 = f2.readlines()
            for i in range(len(lines1)):
                f.write(lines1[i][0] + '\t' +lines2[i][0] + '\n')


