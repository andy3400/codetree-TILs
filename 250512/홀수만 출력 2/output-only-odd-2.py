def main(A, B):
    for i in range(A, B-1, -2):
        print(i, end=' ')

A, B = map(int, input().split())
main(A, B)