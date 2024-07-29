def cal_yune(n):
    if n % 4 == 0:
        if n%100 == 0 and n% 400 != 0:
            return "false"
        return "true"
    return "false"



def main():
    n = int(input())
    print(cal_yune(n))



if __name__=="__main__":
    main()