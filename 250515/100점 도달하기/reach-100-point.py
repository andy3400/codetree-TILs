N = int(input())

while N <=100:
    if N >= 90:
        print("A", end=" ")
    
    elif 90 > N >=80:
        print("B", end=" ")
    
    elif 80 > N >=70:
        print("C", end=" ")

     elif 70 > N >=60:
        print("D", end=" ")

     elif 60 > N :
        print("F", end=" ")
    
    
    N+=1