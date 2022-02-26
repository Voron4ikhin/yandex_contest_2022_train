def factorial(n):
	if n == 0:
		return 1
	elif n == 1:
		return 1
	elif n < 0:
		return -1
	else:
		return n*factorial(n-1)


def number_of_combinations(n, k):
	if n < k:
		return 0
	else:
		return factorial(n)/(factorial(k) * factorial(n-k))


def function(n):
	answer = 0
	for k in range(n + 1):
		answer += ((-1)**k)*number_of_combinations(n, k) * (2**(number_of_combinations(n-k,2)))
	return answer


def answer(n):
	return int(n*function(n-1))

n = int(input())
print(answer(n))

