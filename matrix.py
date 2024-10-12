n = 10
m = 20
a = ()
for i in range(n):
    for j in range(m):
        if i > j :
            a[j][j] = 2
        elif i == j :
            a[i][j] = 1
        else:
            a[i][j] = 0

print(a)
