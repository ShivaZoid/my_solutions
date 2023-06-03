b = str(input())

a = ' '.join([input() for i in range(3)]).split()

q, w = b, a[2]

w = float(w) * 2

book = []

book.append(q)
book.append('Пушкин')
book.append(w)

print(book)
