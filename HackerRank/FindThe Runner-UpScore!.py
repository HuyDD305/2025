if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    x = sorted(list(set(arr)), reverse=True)
    print(x[1])




