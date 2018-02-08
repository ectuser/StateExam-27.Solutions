N = int(input())
'''
Задача: посчитать кол-во пар элементов,
произведение которых делится на 58

-----------------------------------

Произведение делится на 58, если
один из членов делится на 58, либо если
один из членов делится на 2, а второй на 29'''
k58 = 0 #кол-во эл, делящихся на 58
k2 = 0 #кол-во эл, делящихся на 2
k29 = 0 #кол-во эл, делящихся на 29
count = 0 #кол-во произв % 58 == 0
for i in range(N):
	a = int(input())
	if a % 58 == 0:
		k58 += 1
	elif a % 2 == 0:
		k2 += 1
	elif a % 29 == 0:
		k29 += 1
if k58 > 0:
	count = N * k58 - k58
if k2 > 0 and k29 > 0:
	count += k2 * k29
print(count)
