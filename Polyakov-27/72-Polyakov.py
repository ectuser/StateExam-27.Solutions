N = int(input())
'''
Задача: найт  и вывести наибольший общий делитель,
встретившийся наибольшее количество раз.
Или несколько, если таких несколько. 

-------------------------------------------------

Создаем массив из НОДов, в который будем записывать
количество таких НОДов, в которых индекс и есть 
сам НОД. 

Так как часла меньше 10001,то НОД этих чисел < 10001.

В цикле мы проходим алгоритм Евклда, опред НОД.
Далее в ячейку с индексом, равным НОД прибавляем 1.

Далее дважды проходим цикл, первый раз считая макс
НОД, а второй определяя, если ли еще такой НОД, 
поэтому ВТОРОЙ РАЗ ЦИКЛ ПРОХОДИМ С КОНЦА. 
'''
NOD = [0]*10001
for i in range(N):
	a = int(input())
	b = int(input())
	nodInCircle = 10001 # НОД в цикле
	while a != 0 and b != 0:
		if a > b:
			a %= b
		else:
			b %= a
	nodInCircle = a + b 
	# алгоритм Евклида для нахождения НОД
	NOD[nodInCircle] += 1 # к элементу с индексом ,
	# равным НОДу прибавляем 1 
maxNod = -1 # макс НОД
for i in range(10001):
	if NOD[i] > maxNod:
		maxNod = NOD[i]
		# ищем макс НОД
i = 10000
while i > 0:
	if NOD[i] == maxNod:
		print(i, end=" ") # ВЫВОДИМ ИНДЕКС, так как
		# индекс = НОД
	i -= 1
	# ищем другие индексы максимального НОДа