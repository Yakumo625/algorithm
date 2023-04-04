from collections import deque

code = ''.join(input().split())
q, d = deque(), set()

q.append(code)
d = {code : 0}

while q:

	old_code = q.popleft()
	p = old_code.find('x')
		
	for dx, jud in [(3, -1), (-1, -1), (1, 0), (-1, 1)]:
		if (p + 1) % 3 == jud: continue
		px = p + dx
		if px < 0 or px >= 9: continue

		vp, vpx = old_code[p], old_code[px]
		new_code = old_code[:p] + vpx + old_code[p + 1:]
		new_code = new_code[:px] + vp + new_code[px + 1:]

		if new_code in d: continue
		
		print(new_code)
		q.append(new_code)
		d[new_code] = d[old_code] + 1
		
		if new_code == '12345678x':
		    print(d[new_code])
		    exit()

print(-1)