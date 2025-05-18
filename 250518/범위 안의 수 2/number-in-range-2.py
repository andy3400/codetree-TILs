arr = []

for _ in range(10):
    arr.append(int(input()))

sum = 0
avg = 0.0
count = 0

for i in arr:
    if 200 >= i and i > 0:
        sum+=i
        count+=1

avg = sum/count

print(f'{sum} {avg:.1f}')