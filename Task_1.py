n = int(input())

if n // 1000 + n % 10 == (n % 1000) // 100 + ((n % 1000) % 100) // 10:
    print('YES')

else:
    print('NO')
