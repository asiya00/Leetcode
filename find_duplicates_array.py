from typing import List


def findDuplicates(nums: List[int]) -> List[int]:
    # di = {}
    # li = []
    # for i in nums:
    #     if i in di:
    #         di[i] += 1
    #         li.append(i)
    #     else:
    #         di[i] = 1
    # return list(set(li))
    ans = []        # arr = [-4, -3, -2, -7, 8, 2, -3, -1]
    for i in range(len(nums)):
        b = abs(nums[i]) - 1       # b = 3, 2, 1, 6, 7, 2, 
        if nums[b] < 0:             
            ans.append(abs(nums[i])) # ans = [2, 3]
        else:
            nums[b] = -nums[b]
    return ans


print(findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
