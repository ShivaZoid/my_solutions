a, b, c, d = map(int, input().split())


if c < a - 1 and d < b - 1:
    print('ДА')
elif d < a and c < b:
    print('ДА')
else:
    print('НЕТ')
