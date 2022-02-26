def concatination(a1, a2):
	list1 = [int(x) for x in reversed(a1)]
	list2 = [int(x) for x in reversed(a2)]
	result_list = []
	i = 0
	dop = 0
	while i < len(list1) and i  <  len(list2):
		result_list.append((list1[i] + list2[i] + dop) % 10)
		dop = (list1[i] + list2[i])//10
		i += 1
	if i == len(list1):
		for j in range(len(list2) - i):
			result_list.append((list2[j + i] + dop) % 10)
			dop = (list2[j + i] + dop) // 10
	if i == len(list2):
		for j in range(len(list1) - i):
			result_list.append((list1[j + i] + dop) % 10)
			dop = (list1[j + i] + dop) // 10
	if dop != 0:
		result_list.append(dop)

	return([x for x in reversed(result_list)])

def subtraction(a1, a2):
	list1 = [int(x) for x in reversed(a1)]
	list2 = [int(x) for x in reversed(a2)]
	result_list = []
	j = 0
	dop = 0
	
	while  j < len(list1) and j  <  len(list2):
		if list1[j] - dop < list2[j]:
			result_list.append(list1[j] + 10 - list2[j] - dop)
			dop = 1
		else:
			result_list.append(list1[j] - list2[j] - dop)
			dop = 0
		j += 1
	if j < len(list2):
		result_list = subtraction(a2,a1)
		result_list[-1] = result_list[-1] * (-1)
	if j < len(list1):
		for i in range(len(list1) - j):
			result_list.append((list1[j + i] - dop))
			dop = 0
	if dop != 0:
		result_list = subtraction(a2,a1)



		result_list[-1] = result_list[-1] * (-1)
		
	return([int(x) for x in reversed(result_list)])	

def multiplication(a1, a2):
	list1 = [int(x) for x in reversed(a1)]
	list2 = [int(x) for x in reversed(a2)]
	result_list = []
	i = 0
	dop = 0
	for j in range(len(list2)):
		promej = []
		for k in range(j):
			promej.append(0)
		for i in range(len(list1)):
			promej.append((list1[i] * list2[j] + dop) % 10)
			dop = (list1[i] * list2[j] + dop) // 10
		if dop != 0:
			promej.append(dop)
			dop = 0
		result_list.append(promej)
	print(result_list)
	for i in range(len(result_list) - 1):
		result_list[0] = concatination([x for x in reversed(result_list[0])], [x for x in reversed(result_list[i + 1])])
	return([x for x in reversed(result_list[0])])

def division(a1, a2):
	result_list = [0]
	print(a1[0])
	while a1[0] > 0:
		a1 = subtraction(a1,a2)
		result_list = concatination(result_list,1)
	return result_list


a1 = input()
a2 = input()
#сложение
#g1 = concatination(a1, a2)
#print(g1)
#for i in range(len(g1)):
#	print(g1[i], end = '')

#вычитание
#g2 = subtraction(a1, a2)
#for i in range(len(g2)):
#	print(g2[i], end = '')

#умножение
#g3 = multiplication(a1, a2)
#for i in range(len(g3)):
#	print(g3[i], end='')

#деление
g4 = division(a1, a2)
print(g4)
