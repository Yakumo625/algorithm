from collections import deque
from collections import defaultdict as ddict
from copy import copy

start = [i for i in '012345678']
end = '087654321'

dx = [-2, -1, 1, 2]

def bfs():
	q = deque()
	q.append((start, 0))
	d = ddict(int)

	while q:
		state, p = q.popleft()
		state_str = ''.join(state)

		for xx in [p + c for c in dx]:
			if xx < 0: xx = 9 + xx
			if xx > 8: xx %= 9

			backup = copy(state)
			backup[p], backup[xx] = backup[xx], backup[p]
			new_state_str = ''.join(backup)

			if d[new_state_str] != 0: continue

			q.append((backup, xx))
			d[new_state_str] = d[state_str] + 1

			if new_state_str == end: return d[new_state_str]
	return -1

print(bfs())