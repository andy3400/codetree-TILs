A, B = map(int, input().split())

print(A, end= " ")
while A < B:
    if A%2!=0:
        A*=2
        print(A, end= " ")
    elif A%2==0:
        A+=3
        print(A, end= " ")
