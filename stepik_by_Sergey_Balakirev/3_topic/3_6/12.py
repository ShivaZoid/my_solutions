lst = ["Москва", "Тверь", "Вологда"]

a = list(map(str.strip, input().split()))

print(*lst + a)
