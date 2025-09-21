def lis_length(nums):
    n = len(nums)
    gb = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                gb[i] = max(gb[i], gb[j] +1)
    print(max(gb))

lis_length([10,9,2,5,3,7,101,18])
