N = int(input())
'''
Найти цифры, встречающиеся чаще всего.
Если таких чисел несколько, то вывести в порядке
убывания
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
