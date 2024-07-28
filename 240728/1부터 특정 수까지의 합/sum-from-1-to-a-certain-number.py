def total_Sum(n):
    sum = 0
    i = 1
    for i in range(n+1):
        sum +=i
        
    return sum/10

def main():
    n = int(input())
    print("%d"%total_Sum(n))

if __name__ == "__main__":
    main()