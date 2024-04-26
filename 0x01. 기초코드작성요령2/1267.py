N = int(input())
a = list(map(int, input().split()))

Y = M = 0

for i in a:
    Y += (i // 30 + 1) * 10
    M += (i // 60 + 1) * 15

if Y == M:
    print("Y M", format(Y))
elif Y > M:
    print("M", format(M))
else:
    print("Y", format(Y))
