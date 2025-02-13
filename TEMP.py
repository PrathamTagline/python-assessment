def max_sum(a):
	inc = a[0]
	exc = 0
	for i in a[1:]:
		new_exc = max(inc,exc)
		inc = exc + i
		exc = new_exc
	return max(inc,exc)
max = max_sum([3, 2, 5, 10, 7])
print(max)