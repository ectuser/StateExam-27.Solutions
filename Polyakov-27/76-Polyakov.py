N = int(input())
'''
Найти числа, длина которых встречается реже всего и
вывести минимальную длину
'''
amountOfNumbers = [0 for i in range(10)]
for i in range(N):
	a = int(input())
	numbers = 0
	while a > 0:
		numbers += 1
		a //= 10
	amountOfNumbers[numbers] += 1
minAmount = 10001
numberOfMinAmount = -1
i = 9
while i > 0:
	if amountOfNumbers[i] <= minAmount and amountOfNumbers[i] != 0:
		minAmount = amountOfNumbers[i]
		numberOfMinAmount = i
	i -= 1
print(numberOfMinAmount, minAmount)