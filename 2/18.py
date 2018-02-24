import numpy as np
with open("/Users/Kazuki/programming/100/2/hightemp.txt", "r") as f:
    lines = f.readlines()
    hightemp = np.array(lines[0].split("\t"))
    for i in range(len(lines)):
        if(i == 0): continue
        arr = lines[i].split("\t")
        a = np.array(arr)
        hightemp = np.vstack((hightemp, a))


    sorted_hightemp = hightemp[hightemp[:, 2].argsort(), :]
    print(sorted_hightemp )

