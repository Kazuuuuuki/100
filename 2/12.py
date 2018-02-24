
with open("col1.txt", "x") as f1:
    with open("col2.txt", "x") as f2:
        with open("hightemp.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                f1.write(line[0] + '\n')
                f2.write(line[1] + '\n')

     


