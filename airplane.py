def check(char):
	if char == '.':
		return 0
	else:
		return 1

def need_seat(side, near):
	if side == 'left':
		if near == 'window':
			return 0
		else:
			return 2
	else:
		if near == 'window':
			return 6
		else:
			return 4

def get_the_row(need):
	row = 0
	new_row = 0
	for k in arr_p:
		for i in range(int(num)):
			if need == 0 or need == 4:
				if check(k[need + i]) == 1:
					new_row +=1
					break
			else:
				if check(k[need - i]) == 1:
					new_row +=1
					break
		if new_row == row:
			break
		else:
			row = new_row
	if len(arr_p) >= row + 1:
		return row
	else:
		return -1

def change_str(row_str, need, num):
	list_str = list(row_str)
	for i in range(num):
		if need == 0 or need == 4:
			list_str[i + need] = 'X'
		else:
			list_str[need - i] = 'X'
	return ''.join(list_str)

def change_str2(row_str, need, num):
	list_str = list(row_str)
	for i in range(num):
		if need == 0 or need == 4:
			list_str[i + need] = '#'
		else:
			list_str[need - i] = '#'
	return ''.join(list_str)


def print_string(need, row):
	string_to_plus = ''

	if need == 0 or need == 4:
		for i in range(int(num)):
			string_to_plus = string_to_plus + str(row) + letters[need + i] + ' '
	else:
		for i in reversed(range(int(num))):
			string_to_plus = string_to_plus + str(row) + letters[need - i] + ' '
	return string_to_plus.rstrip()



n = int(input()) 							#кол-во рядов в самолете
arr_p = []
letters = ['A', 'B', 'C', '_', 'D', 'E', 'F']
for i in range(n):
	p = input()
	arr_p.append(p)

m = int(input())							#кол-во групп пассажиров
for i in range(m):
	num, side, near = input().split()
	need = need_seat(side, near)
	row = get_the_row(need)
	if row == -1:
		print('Cannot fulfill passengers requirements')
	else:
		arr_p[row] = (change_str(arr_p[row], need, int(num)))
		print('Passengers can take seats: ' + print_string(need, row + 1))
		for i in range(len(arr_p))	:
			print(arr_p[i])
		arr_p[row] = (change_str2(arr_p[row], need, int(num)))