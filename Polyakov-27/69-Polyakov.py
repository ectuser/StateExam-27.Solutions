N = int(input())
'''
Вводятся числа. Нужно определить, какая сумма цифр введенных чисел
встречается чаще всего.
'''
Sum = [0]*37
for i in range(N):
	a = int(input())
	s = 0
	while a > 0:
		s += a % 10
		a //= 10
	Sum[s] += 1
maxAmount = -1
numberOfMaxAmount = -1
for i in range(37):
	if Sum[i] > maxAmount:
		maxAmount = Sum[i]
		numberOfMaxAmount = i
print(numberOfMaxAmount)

