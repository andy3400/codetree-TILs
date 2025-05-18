N = int(input())
arr = []

for _ in range(N):
    arr.append(int(input()))

count = 0

for i in arr:
    if i % 2 != 0 and i % 3 == 0:
        count+=i

print(count)