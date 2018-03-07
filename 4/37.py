import func4 as f
import matplotlib.pyplot as plt
data = f.frequency()

left = []
right = []

for i in range(10):
    left.append(data[i][0])
    right.append(int(data[i][1]))

plt.bar([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], right, tick_label=left)
plt.show()

# import matplotlib
# from matplotlib import rc
# print(matplotlib.get_cachedir())