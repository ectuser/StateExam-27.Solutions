N = int(input())
'''
Задача: выбрать из каждой пары число так, чтобы
сумма всех этих чисел была максимально возможной
и не делилась на 5
'''
maxSum = 0
minModule = 10000*2+1
for i in range(N):
	a = int(input())
	b = int(input())
	if a > b:
		maxSum += a
	else:
		maxSum += b
	if abs(a - b) % 5 != 0 and abs(a - b) < minModule:
		minModule = abs(a-b)
if maxSum % 5 == 0:
	print(maxSum - minModule)
else:
	print(maxSum)