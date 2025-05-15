C, N = input().split()
N = int(N)

if C == 'A':
    for i in range(N):
        print(i+1, end=' ')

elif C == 'D':
    for i in range(N, 0, -1):
        print(i, end= ' ')