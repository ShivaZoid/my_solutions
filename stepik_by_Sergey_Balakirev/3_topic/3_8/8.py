a = list(map(int, input().split()))

b = (a[-1] % 2 != 0)

a.pop()

print(*a, b)
