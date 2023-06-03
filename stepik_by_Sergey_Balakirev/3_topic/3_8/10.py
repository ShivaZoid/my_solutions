a = list(map(str.strip, input().split()))

a.sort()
a.pop(0)

print(*a)
