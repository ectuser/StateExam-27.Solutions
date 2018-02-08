N = int(input())
minSum = 0
minModule = 1000
'''
Задача: найти и выбрать из каждой тройки одно
число так, чтобы сумма квадратов этих чисел 
была четной и при этом минимально возможной
---------------------------------------
Сначала считаем нечетный минимальный модуль.
Далее считаем минимальную сумму квадратов, и если 
она нечетная, то прибавляем нечетный
минимальный модуль
'''
for i in range(N):
	a = []
	a.append(int(input()))
	a.append(int(input()))
	a.append(int(input()))
	for x in range(3):
		for k in range(x,3):
			if a[x] > a[k]:
				t = a[x]
				a[x] = a[k]
				a[k] = t
	minSum += a[0] * a[0]
	if abs(a[0]*a[0] - a[1]*a[1]) % 2 != 0 and abs(a[0]*a[0] - a[1]*a[1]) < minModule:
		minModule = abs(a[0]*a[0] - a[1]*a[1])
	if abs(a[0]*a[0] - a[2]*a[2]) % 2 != 0 and abs(a[0]*a[0] - a[2]*a[2]) < minModule:
		minModule = abs(a[0]*a[0] - a[2]*a[2])
if minSum % 2 != 0:
	print(minSum + minModule)
else:
	print(minSum)


