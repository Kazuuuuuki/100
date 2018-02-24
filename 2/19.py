import numpy as np

with open("/Users/Kazuki/programming/100/2/hightemp.txt", "r") as f:
    lines = f.readlines()
    line_row = np.array((lines[0].split("\t"))[0])
    for i in range(len(lines)):
        if(i == 0): continue
        line_row = np.append(line_row, (lines[i].split("\t"))[0])

    u, c = np.unique(line_row, return_counts=True)
    countup_arr = np.array([[u[0], int(c[0])]])
    for i in range(len(u)):
        if(i == 0): continue
        tmp = np.array([[u[i], int(c[i])]])
        countup_arr = np.r_[countup_arr, tmp]

    sorted_countup_arr = countup_arr[countup_arr[:, 1].astype(np.int8).argsort()[::-1], :]
    print(sorted_countup_arr)



