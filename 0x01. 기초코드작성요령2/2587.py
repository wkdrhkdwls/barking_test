
M = []
for _ in range(5):
    a = int(input())
    M.append(a)
M.sort()

print(round(sum(M)/5))
print(M[2])