def all_len(arr):
	dist = []
	for i in range(len(arr)):
		part = []
		for j in range(len(arr)):
			if i == j:
				continue
			part.append(abs(arr[i]- arr[j]))
		dist.append(part)
	return dist

n, k = input().split()
a = input().split()
int_lst = [int(x) for x in a]
final = []
for i in all_len(int_lst):
	final.append(sum(sorted(i)[:int(k)]))

final_str = ''
for i in final:
	final_str = final_str + str(i) + ' '
print(final_str.rstrip())

