t = [
    ["Скажи-ка", "дядя", "ведь", "не", "даром"],
    ["Я", "Python", "выучил", "с", "каналом"],
    ["Балакирев", "что", "раздавал?"]
]

a = str(input())
z = ' '.join(t[0])
h = ' '.join(t[1])
l = ' '.join(t[2])

n = z + h + l

print(a in n)