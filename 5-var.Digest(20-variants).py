N = int(input())
'''
Задача: выбрать из каждой пары число так,
чтобы сумма квадратов всех выбранных чисел была
максимально возможной и не делилась на 3
'''
maxSum = 0
minModule = 100*2+1
for i in range(N):
	a = int(input())
	b = int(input())
	if a > b:
		maxSum += a * a
	else:
		maxSum += b * b
	if abs(a * a - b * b) % 3 != 0 and abs(a * a - b * b) < minModule:
		minModule = abs(a * a - b * b)
if maxSum % 3 == 0:
	print(maxSum - minModule)
else:
	print(maxSum)