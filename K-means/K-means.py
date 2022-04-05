import numpy as np

def Distance(a, b):
    d = (a[0] - b[0])*(a[0] - b[0]) + (a[1] - b[1])*(a[1] - b[1]) + (a[2] - b[2])*(a[2] - b[2]) + (a[3] - b[3])*(a[3] - b[3])
    return d

data = np.loadtxt("iris.csv", delimiter=",", dtype=np.float32, skiprows=1)

mean = np.array([[5.1, 4.0, 1.3, 0.1], [5.0, 3.3, 1.5, 0.3], [4.7, 3.5, 1.6, 0.6]])
p = np.zeros(4)
d = np.zeros(3)

sum = np.zeros((3,4))
num = np.zeros(3)

for epoch in range(10):
    #Grouping
    for i in range(150):
        for j in range(4):
            p[j] = data[i][j+1]

        for j in range(3):
            d[j] = Distance(mean[j], p)
        minldx = np.argmin(d)

        for j in range(4):
            sum[minldx][j] += p[j]
        num[minldx] += 1

    #Adjustment
    print("point :: ", epoch)

    for i in range(3):
        if num[i] != 0:
            for j in range(4):
                mean[i][j] = sum[i][j] / num[i]

    print("Mean :: ", mean)
    print("Sum :: ", sum)
    print("Num :: ", num)

    for i in range(3):
        for j in range(4):
            sum[i][j] = num[i] = 0
