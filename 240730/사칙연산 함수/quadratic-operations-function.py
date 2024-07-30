def trans(a, b, c):
    a = int(a)
    c = int(c)

    if b == "*":
        result = a * c
        show = f"{a} {b} {c} = {result}"
        return show
    elif b == "+":
        result = a + c
        show = f"{a} {b} {c} = {result}"
        return show
    elif b == "-":
        result = a - c
        show = f"{a} {b} {c} = {result}"
        return show
    elif b == "/":
        result = a // c  # 나눗셈 결과를 정수로 표시
        show = f"{a} {b} {c} = {result}"
        return show

def main():
    a, b, c = input().split()
    result = trans(a, b, c)
    if result:
        print(result)
    else:
        print("False")

if __name__ == "__main__":
    main()