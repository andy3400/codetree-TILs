arr = []

cnt3  = 0
cnt5  = 0

for _ in range(10):
    arr.append(int(input()))

for i in arr:
    if i % 3 == 0:
        cnt3 +=1
for i in arr:
    if i % 5 == 0:
        cnt5 +=1 

print(f'{cnt3} {cnt5}')