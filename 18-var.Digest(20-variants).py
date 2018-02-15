N = int(input())
'''
Задача: найти максимальную нечетную сумму элементов
и вывести их номра

-------------------------------------------------

Чтобы сумма была нечетной необходимо, 
чтобы количество нечетных элементов была нечетной.
Считаем количество нечетных элементов, номер 0,
номер минимального нечетного. 
Если нечетных четное количество, то выводим все
кроме минимального нечетного и 0.
Если четное, то выводим все, кроме 0. 
'''
zeroPos = -1
minNot2 = 1000000001
minNot2Pos = -1
not2Counter = 0
for i in range(1,N+1):
	a = int(input())
	if a == 0:
		zeroPos = i
	if a % 2 != 0:
		not2Counter += 1
		if a < minNot2:
			minNot2 = a
			minNot2Pos = i
if not2Counter % 2 == 0:
	for i in range(1,N+1):
		if i != zeroPos and i != minNot2Pos:
			print(i, end=" ")
else:
	for i in range(1,N+1):
		if i != zeroPos:
			print(i, end=" ")


