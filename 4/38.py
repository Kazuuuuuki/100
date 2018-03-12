import func4 as f
import matplotlib.pyplot as plt
data = f.frequency()

right = []
for i in range(len(data)):
    right.append(data[i][1])

plt.hist(right, bins=20, range=(1, 20))
plt.xlim(xmin=1, xmax=20)

plt.show()



