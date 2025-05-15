A, B = map(int, input().split())

if A < B:
    for B in range(B, A-1, -1):
        print(B, end = " ")
else:
    for A in range(A, B-1, -1):
        print(A, end=" ")

