from collections import Counter

N = int(input())
card = list(map(int, input().split()))
card_count = Counter(card)
M = int(input())
answer = list(map(int, input().split()))

result = []
for i in answer:
    result.append(card_count[i])

print(" ".join(map(str, result)))
