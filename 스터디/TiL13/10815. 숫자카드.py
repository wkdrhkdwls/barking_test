from bisect import bisect_left

def calCount(nums, value):
    idx = bisect_left(nums,value)
    return idx < len(nums) and nums[idx] == value

N = int(input())
card = list(map(int, input().split()))
card.sort()
M = int(input())
answer = list(map(int, input().split()))

result = []
for value in answer:
    if calCount(card,value):
        result.append(1)
    else:
        result.append(0)

print(" ".join(map(str,result)))