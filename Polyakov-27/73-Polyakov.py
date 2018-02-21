N = int(input())
'''
Найти и выбрать из каждой тройки одно число так,
чтобы сумма всех чисел не делилась на 4

------------------------------------------------

Находим максимальную сумму и ищем минимальную
разность, которая при делении на 4 != 0.
Если макс сумма % 4 == 0, то вычитаем мин разность.
'''
maxSum = 0 # максимальная сумма 
minDeltaNot4 = 10001 # мин разность % 4 != 0
a = [10001]*3
for i in range(N):
	a[0] = int(input())
	a[1] = int(input())
	a[2] = int(input())
	for x in range(3):
		for k in range(x,3):
			if a[k] > a[x]:
				t = a[x]
				a[x] = a[k]
				a[k] = t
				# сортировка
	maxSum += a[0]
	if (a[1] - a[2]) % 4 != 0 and (a[1] - a[2]) < minDeltaNot4:
		minDeltaNot4 = (a[1] - a[2])
	if (a[0] - a[2]) % 4 != 0 and (a[0] - a[2]) < minDeltaNot4:
		minDeltaNot4 = (a[0] - a[2])
	# определяем минимальную разность
if maxSum % 4 == 0:
	print(maxSum - minDeltaNot4)
else:
	print(maxSum)


