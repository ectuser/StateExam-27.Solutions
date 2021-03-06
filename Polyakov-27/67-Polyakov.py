N = int(input())
'''
Найти цифры, встречающиеся чаще всего.
Если таких чисел несколько, то вывести в порядке
убывания

-------------------------------------------------

Вводим массив, где индекс - цифра, а значение - 
кол-во таких цифр.
Вводим число, определяем цифры и к соответств
элементам прибавляем 1.

Далее прогоняем массив 1 раз, чтобы подсчитать 
макс кол-во элементов и еще один раз с конца, 
чтобы вывести элементы, в которых значение равно 
максимальному, то есть от большего к меньшему.
'''
numbers = [0]*10
for i in range(N):
	a = int(input())
	while a > 0:
		numbers[a % 10] += 1
		a //= 10
maxAmount = 0
for i in range(10):
	if numbers[i] > maxAmount:
		maxAmount = numbers[i]
for i in range(9,-1,-1):
	if numbers[i] == maxAmount:
		print(i, end=" ")
