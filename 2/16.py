import sys
import math
args = sys.argv
with open("hightemp.txt", "r") as f:
    lines = f.readlines()
    l = [(len(lines) + i) // int(args[1]) for i in range(int(args[1]))]
    j = 0
    for x in range(int(args[1])):
        f = open('hightemp-split' + str(x) + '.txt', 'x')
        for i in range(l[x]):
           f.write(lines[i+j])
           
        j = j+l[x]
        f.close



