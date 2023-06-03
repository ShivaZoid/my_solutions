a = ' '.join([input() for i in range(2)]).split()

b = float(a[1]) / float(a[0])

print(f'Вы можете получить {int(b)}$ за {a[1]} рублей по курсу {a[0]}')
