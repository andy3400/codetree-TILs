a, b = map(int, input().split())

def cal(a,b):
    min_num = min(a, b)
    max_num = max(a, b)

    print(f"{min_num + 10} {max_num * 2}")

cal(a,b)
