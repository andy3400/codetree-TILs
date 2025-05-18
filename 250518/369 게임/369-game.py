N = int(input())

for i in range(1, N+1):
    #  3의 배수인 3, 6, 9 가 나와야 한다. 
    #  10을 나누는 조건문을 통해 3, 6, 9 확인.
    #  이후, 있으면 0을 출력

    if i > 10:
        if i // 10 == 3 or i // 10 == 6 or i // 10 == 9 or i % 3 == 0:
            print("0", end= ' ')

        elif i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
            print("0", end= ' ')

        else:
            print(i, end=" ")
    else:
        if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
            print("0", end= ' ')
        else:
            print(i, end=" ")

