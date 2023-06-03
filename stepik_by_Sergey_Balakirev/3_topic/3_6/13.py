cities = ['Москва', 'Тверь', 'Вологда']

lst = list(map(str.strip, input().split()))

a = lst + cities

print(*a)
