n = int(input())
arr = list(map(int, input().split()))


for i in range(len(arr)):
    if arr[i] % 2 == 0:
        arr[i] = int(arr[i]/2)
    else:
        arr[i] = arr[i]

for enum in range(len(arr)):
    print(arr[enum], end= " ")