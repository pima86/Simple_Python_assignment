import numpy as np

data = np.loadtxt("data.txt", delimiter=",", dtype=np.float32)
print(data)

irisData = {}
irisData[0] = data[:]

sum = 0

for j in range (3):
    for i in range (5):
        sum += irisData[0][i][j]
        
    avg = sum/5
    print(j,"열의 평균 : ", sum, avg)