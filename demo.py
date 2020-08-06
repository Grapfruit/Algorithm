def rec_opt(arr, n, last=None):
    if n == 0:
        return min(arr[0][0], arr[0][1], arr[0][2])

    if n > 0:
        if last == None:
            A = arr[n][0] + rec_opt(arr, n-1, 0)
            B = arr[n][1] + rec_opt(arr, n-1, 1)
            C = arr[n][2] + rec_opt(arr, n-1, 2)
            return min(A, B, C)
        else:
            choose = []
            for i in range(3):
                if i != last:
                    choose.append(arr[n][i] + rec_opt(arr, n-1, i))
            return min(choose)


if __name__ == "__main__":
    arr = []
    n = int(input())

    for _ in range(n):
        i = input().split()
        s = []
        for j in i:
            s.append(int(j))
        arr.append(s)

    print(arr)
    print(rec_opt(arr, n-1))
