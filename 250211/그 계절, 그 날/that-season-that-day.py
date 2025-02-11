Y, M, D = map(int, input().split())

# Write your code here!
#윤년 계산
def date_cal(Y, M, D):
    # 윤년 계산
    if (Y % 4 == 0 and Y % 100 != 0) or (Y % 400 == 0):
        if M == 2:
            return 29
        else:
            return 31 if M in[1,3,5,7,8,10,12] else 30
    else:
        if M == 2:
            return 28
        else:
            return 31 if M in[1,3,5,7,8,10,12] else 30

#계절 계산
def season_cal(Y, M, D):
    if D>date_cal(Y,M,D):
        print("-1")

    else:
        if M in range(3, 6):
            print("Spring")
        elif M in range(6, 9):
            rrint("Summer")
        elif M in range(9, 12):
            print("Fall")
        elif M in (12,1,2):
            print("Winter")
        else:
            print("-1")

season_cal(Y,M,D)