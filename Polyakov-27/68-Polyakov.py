N = int(input())
'''
Вводятся числа. Необходимо определить, с какой цифры
реже всего начинаются числа. Если таких чисел
несколько, то нужно вывести минимальное.

Создаем массив, где индекс - цифра а знач - кол-во
таких цифр. Вбиваем число, определяем первую цифру.
К соотв элементу прибавляем 1. 

Далее прогоняем цикл от конца, чтобы найти мин.
'''
numbers = [0]*10
for i in range(N):
	a = int(input())
	while a > 0:
		number = a % 10
		a //= 10
	numbers[number] += 1
minNumber = 1001
indexOfMinNumber = -1
for i in range(9,0,-1):
	if numbers[i] <= minNumber and numbers[i] != 0:
		minNumber = numbers[i]
		indexOfMinNumber = i
print(indexOfMinNumber)