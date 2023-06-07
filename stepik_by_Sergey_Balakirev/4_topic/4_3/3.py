m = str(input())
m = m.lower()

d = 'палиндром' if m == m[::-1] else 'не палиндром'

print(d)
