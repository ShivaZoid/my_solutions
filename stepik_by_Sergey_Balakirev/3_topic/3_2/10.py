a, b = map(str, input().split())

l = len(b)

print(a[1:l:2] == b[1::2])
