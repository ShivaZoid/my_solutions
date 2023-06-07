m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']

dit = {}

for i, n in enumerate(m):
    if n == 'до':
        dit[i+1] = '#' + n
    elif n == 'фа':
        dit[i+1] = '#' + n
    else:
        dit[i+1] = n

f = list(map(int, input().split()))

print(dit[f[0]], dit[f[1]], dit[f[2]])
