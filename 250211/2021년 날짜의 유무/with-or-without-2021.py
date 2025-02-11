M, D = map(int, input().split())

# Write your code here!
def cal(M,D):
    D_28 = (2, )
    D_30 = (4,6,9,11)
    D_31 = (1,3,5,7,8,10,12)

    if M in D_28:
        if D <=28:
            print("Yes")
        else:
             print("No")      
    elif M in D_30:
        if D<=30:
            print("Yes")
        else:
             print("No") 
    elif M in D_31:
        if D<=31:
            print("Yes")  
        else:
            print("No") 
    else:
        print("No") 

cal(M,D)