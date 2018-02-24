import sys
args = sys.argv
with open("hightemp.txt", "r") as f:
    lines = f.readlines()
    i = len(lines)
    print(lines[i - 1 -  int(args[1])])


