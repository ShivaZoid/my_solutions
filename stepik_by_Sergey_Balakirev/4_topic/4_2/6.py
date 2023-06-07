m, n = map(int, input().split())

# Определяем число дней в каждом месяце
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# предыдущий день
prev_m = m - 1
prev_n = n - 1
if prev_n == 0:
    prev_m -= 1
    prev_n = days_in_month[prev_m]

# следующий день
next_m = m - 1
next_n = n + 1
if next_n > days_in_month[next_m]:
    next_m += 1
    next_n = 1


print("{:02d}.{:02d} {:02d}.{:02d}".format(prev_m + 1, prev_n, next_m + 1, next_n))
