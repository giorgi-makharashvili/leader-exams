def max_product(nums):
    max1 = max(nums[0], nums[1])
    max2 = min(nums[0], nums[1])

    for i in nums:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2:
            max2 = i
    print(max1 * max2)

max_product([1,2,3,4])