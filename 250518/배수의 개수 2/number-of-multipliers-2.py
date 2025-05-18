arr = []
count = 0

for _ in range(10):
    arr.append(int(input()))

for i in arr:
    if i % 2 != 0:
        count+=1

print(count)