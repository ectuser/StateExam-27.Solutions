N = int(input())
'''
Вводятся числа. Нужно определить, какая сумма цифр 
веденных чисел встречается чаще всего.

------------------------------------------------

Так как Каждое число не превышает 1000, то
максимальная сумма цифр числа может быть 9+9+9=27.

Создаем массив из 28 эл-тов [0..27]. Далее вводим
числа, определяем введенную сумму и добавляем 
к лементу с индексом = сумме 1. 

Далее находим индекс чаще всего встречающейся суммы
и выводим его. Проходим цикл С КОНЦА, так как если
чаще всего встречающихся сумм будет несколько, то 
необходимо будет вывести НАИБОЛЬШУЮ из них.
'''
Sum = [0]*28 # массив из 28 эл [0..27]
for i in range(N):
	a = int(input())
	s = 0
	while a > 0:
		s += a % 10
		a //= 10
		# подсчитываем сумму цифр
	Sum[s] += 1 # к индексу=сумме цифр прибавляем 1
maxAmount = -1
numberOfMaxAmount = -1
for i in range(27,0,-1):
	if Sum[i] > maxAmount:
		maxAmount = Sum[i]
		numberOfMaxAmount = i
		# проходим цикл с конца и находим макс
		# элемент с наибольшим индексом, если таких
		# элементов несколько
print(numberOfMaxAmount)

