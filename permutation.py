def permute(nums):
	if len(nums) == 0:
		return []
	if len(nums) == 1:
		return [nums]
	li = []
	for i in range(len(nums)):
		selected_ele = nums[i]
		li1 = nums[:i] + nums[i+1:]

		for j in permute(li1):
			li.append([selected_ele]+j)
	return li

print(permute([1, 2, 3]))