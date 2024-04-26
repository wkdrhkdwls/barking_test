M = []
for _ in range(7):
    a = int(input())
    if a % 2 != 0:  # 홀수면
        M.append(a)  # 배열에 넣는다.

if len(M) == 0:
    print(-1)
else:
    print(sum(M))
    print(min(M))
