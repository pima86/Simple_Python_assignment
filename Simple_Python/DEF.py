def 합구하기(num):
    hap = 0
    for i in range(1, num+1, 1):
        hap = hap + i
    return hap

print(합구하기(10))
