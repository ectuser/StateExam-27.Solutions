N = int(input())
'''
Задача: найти минимальное произведение элементов и 
вывести их номера
'''
minusCounter = 0
maxMinus = -1000000001
maxMinusPos = -1
zeroPos = -1
for i in range(1,N+1):
	a = int(input())
	if a < 0:
		minusCounter += 1
		if a > maxMinus:
			maxMinus = a
			maxMinusPos = i
	if a == 0:
		zeroPos = i
for i in range(1,N+1):
	if minusCounter % 2 == 0:
		if i != zeroPos and i != maxMinusPos:
			print(i, end=" ")
	elif i != zeroPos:
		print(i, end=" ")