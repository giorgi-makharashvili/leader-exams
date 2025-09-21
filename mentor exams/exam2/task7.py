def has_subset_sum(nums, target):

    if target == 0:
        return True
    if not nums:
        return False

    lastn = nums[-1]

    if lastn <= target and has_subset_sum(nums[:-1], target- lastn):
        return True
    return has_subset_sum(nums[:-1], target)
    
has_subset_sum([3,34,4,12,5,2], 9)