with open("hightemp.txt", "r") as f:  #　txt形式の読み込み
    data = f.read()

data2 = data.replace("\t"," ")

with open("hightemp2.txt", "x") as f:
    f.write(data2)

