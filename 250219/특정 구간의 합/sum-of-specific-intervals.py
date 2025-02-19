arr = []
prefix = []

def preprocess():
    global prefix
    prefix = [0] * (len(arr) +1)
    for i in range(1, len(arr) + 1):
        prefix[i] = prefix[i-1] + arr [i-1]

def query_sum(a1, a2):
    return prefix[a2] - prefix[a1-1]

def main():
    global arr
    n, m = map( int, input().split())
    arr = list(map(int, input().split()))
    queries = [tuple(map(int, input().split())) for _ in range(m)]

    preprocess()

    for a1, a2 in queries:
        print(query_sum(a1, a2))

main()