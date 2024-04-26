M = []

for _ in range(9):
    a = int(input())
    M.append(a)
M.sort()
sumM = sum(M)

i = 0
while i < len(M) - 1:
    removed = False
    j = i + 1
    while j < len(M):
        if sumM - M[i] - M[j] == 100:
            # 첫 번째 요소를 삭제
            num1 = M[i]
            # 두 번째 요소를 삭제 (i 이후이므로 j는 항상 i보다 큼)
            num2 = M[j]

            # 두 요소를 삭제
            M.remove(num1)
            M.remove(num2)
            removed = True
            break  # 내부 반복문 중단
        j += 1
    if not removed:
        i += 1  # 요소를 삭제하지 않았으면 i를 증가

for a in M:
    print(a)
