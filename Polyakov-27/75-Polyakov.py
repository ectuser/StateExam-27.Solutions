N = int(input())
'''
Задача: количество пар, где произведение элементов
кратно 6
'''
k2 = 0
k3 = 0
k6 = 0
amount = 0
for i in range(N):
	a = int(input())
	if a % 6 == 0:
		k6 += 1
		amount += N - k6
		# либо эта строка всерху
	elif a % 3 == 0:
		k3 += 1
	elif a % 2 == 0:
		k2 += 1
#amount += (N - k6) * k6 + (k6 * (k6 - 1)) // 2
# либо эта срока
amount += k3 * k2
print(amount)
