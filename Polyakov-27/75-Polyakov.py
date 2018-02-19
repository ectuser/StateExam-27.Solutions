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
