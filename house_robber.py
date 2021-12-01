from typing import List
def rob(nums: List[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    dp = []
    dp.append(nums[0])
    dp.append(max(nums[0], nums[1]))
    for i in range(2, len(nums)):
        dp.append(max(nums[i] + dp[i-2], dp[i-1]))
    return dp[-1]


nums = [1, 2, 3, 1]
print(rob(nums))
