a, b = map(str.strip, input().split())

c = ' '.join([a, b]).split()

print(f'{min(c)} {max(c)}')
