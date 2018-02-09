N = int(input())
s = 15 #время между моментами
minPr = 10000*10000+1 #мин пр-е
minElem = 10000000 #минимальный эл без 15 посл
min2 = 1000000 #мин эл %2 == 0
minNot2 = 100000 #мин эл %2 != 0

'''
Задача: найти минимальное четное произведение среди
моментов, между которыми прошло 15 или более
секунд
'''
a = []
for i in range(s):
	a.append(int(input()))
a.append(int(input()))
for i in range(s+1,N):
	elem = int(input())
	if a[0] < minElem:
		minElem = a[0]
		#если первый элемент массива < мин эл
		#без 15 посл
	if a[0] % 2 == 0 and a[0] < min2:
		min2 = a[0]
	if elem % 2 == 0:
		pr = elem * minElem
	elif min2 < 100000:
		pr = elem * min2
	else:
		pr = 1000000
	if pr < minPr:
		minPr = pr
	for i in range(1,s+1):
		a[i-1] = a[i]
	#a[s+1] = elem
print(a)



