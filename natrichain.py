import math
def matchain(p, n):
    m = [[0 for x in range(n)] for x in range(n)]
    for i in range(1, n):
        m[i][i] = 0


    for l in range(2, n):
        for i in range(1, n-l + 1):
            j = i + l-1
            m[i][j] =math.inf
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q

    return m


sizes = [30,35,15,5,10,20,25]
size = len(sizes)
output=matchain(sizes, size)
print(output)
print(output[1][size-1])



