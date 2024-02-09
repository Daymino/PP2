def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


print(has_33([1, 3, 3]))      # Output: True
print(has_33([1, 3, 1, 3]))   # Output: False
print(has_33([3, 1, 3]))      # Output: False