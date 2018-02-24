import sys
args = sys.argv
with open("hightemp.txt", "r") as f:
    lines = f.readlines()
    print(lines[int(args[1])-1])
