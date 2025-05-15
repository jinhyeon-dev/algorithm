input = __import__('sys').stdin.readline

n = int(input())

def check(i):
	global num
	if len(num) == 1: return 1
	if num[-2] > i: return 1
	else: return 0

num = []
ans = []
def dfs(depth):
	global num
	for i in range(10):
		num.append(i)
		if check(i):
			dfs(depth + 1)
			ans.append(int(''.join(str(x) for x in num)))
		num.pop()
	
dfs(0)
ans.sort()

if n >= len(ans): print(-1)
else: print(ans[n])