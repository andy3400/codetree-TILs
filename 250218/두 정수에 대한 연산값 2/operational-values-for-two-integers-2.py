a, b = map(int, input().split())

def cal(a,b):
    min_num = min(a, b)
    max_num = max(a, b)

    if a == min_num:
        a = min_num + 10
        b = max_num * 2
    else:
        a = max_num * 2
        b = min_num + 10
        
    print(f"{a} {b}")

cal(a,b)
