def cal(i):
    if i % 2 == 0 or i%10 == 5 or (i%3 == 0 and i%9!=0):
        return False
    else:
        return True

def repeat(a, b):
    sum = 0
    for i in range(a, b+1):
        if cal(i):
            sum +=1
        else:
            continue
    return sum


def main():
    a, b = map(int, input().split())
    print(repeat(a, b))

if __name__ == "__main__":
    main()