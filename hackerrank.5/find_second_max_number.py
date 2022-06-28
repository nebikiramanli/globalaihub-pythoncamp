def find_second_maximum_number(arr, n):
    mx = max(arr[0], arr[1])
    secondmax = min(arr[0], arr[1])
    for i in range(2, n):
        if arr[i] > mx:
            secondmax = mx
            mx = arr[i]
        elif arr[i] > secondmax and mx != arr[i]:
            secondmax = arr[i]
        elif secondmax == mx:
            secondmax = arr[i]

    return secondmax

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(find_second_maximum_number(list(arr), n))