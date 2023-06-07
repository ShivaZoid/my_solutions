a, b, c = map(int, input().split())

g = a ** 2 + b ** 2

if g == c ** 2:
    print('ДА')
else:
    print('НЕТ')
