n = int(input())
str_ = input()

i = j = xn = res = 0
while j < n:
	if str_[j] != 'x':
		xn = 0
		i = j
	else: xn += 1
	while xn > 2 and i < j:
		if str_[i] == 'x':
			xn -= 1
			res += 1
		i += 1
	j += 1

print(res)