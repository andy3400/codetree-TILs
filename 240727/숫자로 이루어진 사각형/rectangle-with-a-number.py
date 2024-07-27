def printNum(a):
    num = 1
    for _ in range(a):
        for _ in range(a):
            print("%d"%num, end= " ")
            num = num + 1
            if num>9:
                num = 1
        print()
        
def main():
    a = int(input())
    printNum(a)

if __name__ =="__main__":
    main()

# // 입력
# // 반복문을 통해서 n * n 모양 만들기
# // when we meed if, return 1
# // main