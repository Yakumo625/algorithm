from collections import defaultdict as ddict

n = int(input())
words = []
for _ in range(n):
	word = input()
	words.append((word, len(word)))
first = input()

d = ddict(int)

ans = 0

def check(word, next_word, l1, l2):
	l = min(l1, l2)
	for len_ in range(1, l+1):
		if word[l1-len_:] == next_word[:len_]: return len_
	return 0

def dfs(word, l1):
	global ans

	jud = 1
	
	for next_word, l2 in words:
		if d[next_word] > 1: continue

		len_ = check(word, next_word, l1, l2)

		if len_ == 0 or len_ == l1 or len_ == l2: continue
		else:
			jud = 0
			d[next_word] += 1
			new_word = word[:l1 - len_] + next_word
			dfs(new_word, len(new_word))
			d[next_word] -= 1

	if jud:
		ans = max(ans, l1)
		return


for word, l in words:
	if word[0] == first:
		d[word] += 1
		dfs(word, l)
		d[word] -= 1

print(ans)

