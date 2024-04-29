S = input()

arr = [0] * 10

for i in S:
    arr[int(i)] += 1
    if i == '6' and arr[6] > arr[9]:
        arr[9] += 1
        arr[6] -= 1
    elif i == "9" and arr[6] < arr[9]:
        arr[9] -= 1
        arr[6] += 1
print(max(arr))
