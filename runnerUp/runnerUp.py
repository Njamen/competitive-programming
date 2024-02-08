if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = sorted(arr, reverse=True)
    arr = [x for x in arr if x!=arr[0]]
    print(arr[0])
