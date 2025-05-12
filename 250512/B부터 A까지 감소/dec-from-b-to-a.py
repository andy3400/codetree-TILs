def main(A,B):
    for i in range(B, A-1, -1):
        print(i, end= ' ')

A, B = map(int, input().split())
main(A, B)