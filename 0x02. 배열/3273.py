n = int(input())
a = list(map(int, input().split()))

x = int(input())
a.sort()
left, right = 0, n - 1
result = 0

while left < right:
    S = a[left] + a[right]
    if S > x:
        right -= 1
    elif S < x:
        left += 1
    elif S == x:
        result += 1
        left += 1

print(result)