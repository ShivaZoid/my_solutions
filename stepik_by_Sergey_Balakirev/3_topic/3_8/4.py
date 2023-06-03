a = list(input())

a.pop(0)
a.pop(0)
a.insert(0, str(8))
a.pop(9)
a.pop(11)

print("".join(a))
