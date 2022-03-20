sum=0

print("10개의 숫자를 입력하세요 :")

for i in range(10):
	print(format(i), end="번째 숫자 :")
	x = int(input())
	sum += x

print("총합", end="--->")
print(sum)