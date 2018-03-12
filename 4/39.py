import func4 as f
import matplotlib.pyplot as plt
data = f.frequency()

right = []
for i in range(len(data)):
    right.append(data[i][1])

plt.scatter(range(1, len(right) + 1), right)
# plt.xlim(xmin=1, xmax=20)
plt.xlim(1, len(right) + 1)
plt.ylim(1, right[0])

plt.xscale("log")
plt.yscale("log")
plt.show()


