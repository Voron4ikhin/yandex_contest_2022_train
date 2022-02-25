def first():	
	n = int(input())
	arr = input().split()
	for i in range(n):
		if i != 0:
			if int(arr[i]) < int(arr[i - 1]):
				return -1
	return  int(arr[n-1]) - int(arr[0])

print(first())