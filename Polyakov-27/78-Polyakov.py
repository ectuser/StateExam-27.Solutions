N = int(input())
s = 3
'''
Найти количество произведений элементов, кратных 6
между моментами которых прошло 3 и более минут

------------------------------------------------

Проверяем 0-й элемент. Если он кратный 3 или 2 или 6
то прибавляем счетчик к соответственным переменным.
Далее смотрим, если 3-й элемент кратен двум, то
количество чисел увеличивается на k3, если трем, то
на k2, а в конце просто на k6.
'''
a = []
k3 = 0 # количество a[0] кратных 3
k2 = 0 # количество а[0] кратных 2
k6 = 0 # количество а[0] кратных 6
amount = 0 # количество
for i in range(s):
	a.append(int(input()))
	# заполнение массива 3-мя числами
a.append(-1) # добавление 4-го элемента
for i in range(s,N):
	a[s] = int(input())
	if a[0] % 6 == 0:
		k6 += 1
	elif a[0] % 3 == 0:
		k3 += 1
	elif a[0] % 2 == 0:
		k2 += 1
	# ^ проврка на 0-й элемент массива
	if a[s] % 3 == 0:
		amount += k2
	if a[s] % 2 == 0:
		amount += k3
	for x in range(1,s+1):
		a[x-1] = a[x]
	amount += k6
print(amount)