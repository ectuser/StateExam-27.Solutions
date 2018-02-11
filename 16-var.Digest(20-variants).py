N = int(input())
'''
Задача: найти миксимальную сумму показаний,
между моментами которых прошло не менее 10-и 
секунд

---------------------------------------

Короче, просто ищем максимальное a[0] каждый
раз проходя через цикл и сверяем с a[10]
'''
a = []
s = 10
maxSum = -1
maxA0 = -1
for i in range(s):
	a.append(int(input()))
a.append(-1)
for i in range(s,N):
	a[s] = int(input())
	if a[0] > maxA0:
		maxA0 = a[0]
	if maxA0 + a[s] > maxSum:
		maxSum = maxA0 + a[s]
	for x in range(1,s+1):
		a[x-1] = a[x]
print(maxSum)
