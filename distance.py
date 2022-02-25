
n, k = input().split()
a = input().split()
int_lst = [int(x) for x in a]

c = [i for i in range(len(int_lst))]
our_dict = dict(zip(c, int_lst))
list_d = list(our_dict.items())
list_d.sort(key=lambda i: i[1])
g2 = []
for j in range(len(a)):
	g1= []
	for i in range(int(k)):
		if (i + j + 1) >= len(a):
			break
		else:
			g1.append(abs(list_d[j][1] - list_d[i + j + 1][1]))
	for i in range(int(k)):
		if (j - i - 1) < 0:
			break
		else:
			g1.append(abs(list_d[j][1]-list_d[j - i - 1][1]))
	g2.append(g1)
g3 = []
list_d = dict(list_d)
onl_k = list(list_d.keys())
for i in g2:
	g3.append(sum(sorted(i)[:int(k)]))
almost = dict(zip(onl_k, g3))
onl_k.sort()
final = ''
for i in onl_k:
	final = final + str(almost[i]) + ' '
print(final.rstrip())

