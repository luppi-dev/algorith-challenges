def rob(nums: [int]) -> int:
        two_before, one_before = 0, 0
        for current in nums:
            temp = max(current + two_before, one_before)
            two_before = one_before
            one_before = temp
        return one_before
    
print(rob([3, 6, 9, 3, 2, 7]))