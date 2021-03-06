N = int(input())
'''
Найти максимальную возможную четную сумму элементов и
вывести индексы этих элементов

--------------------------------------

Сумма будет максималльно возможной и четной, если 
количество нечетных элементов будет четным.
Короче, считаем количество нечетным элементов
и ищем минимальный вреди них, его позицию, 
а также позицию 0.
При выводе сразу же исключаем 0, а также, если
количество нечетных элементов четное, то
выводим все подряд, а если нечетное, о выводим все
кроме минимального нечетного
'''
s = 0
minNot2 = 10000000001 # минимальное нечетное
minNot2Pos = -1 # позиция минимального нечетного 
zeroPos = -1 # позиция 0
count = 0 # количество нечетных
for i in range(1,N+1):
	a = int(input())
	if a == 0:
		zeroPos = i
	if a % 2 != 0:
		count += 1
		if a < minNot2:
			minNot2 = a
			minNot2Pos = i
for i in range(1,N+1):
	if i != zeroPos:
		if count % 2 == 0:
			print(i, end=" ")
		elif i != minNot2Pos:
			print(i, end=" ")

