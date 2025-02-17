n = int(input())
arr = list(map(int, input().split()))

for i in range(len(arr)):
    print(abs(arr[i]), end= " ")