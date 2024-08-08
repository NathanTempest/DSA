#kadane's algorithm gives us the maximum sum of subarray for an array in linear time

from cmath import inf
def maxSubArray(nums):
    max_sum = float(-inf)
    curr_sum = max_sum
    for i in nums:
        if i > (i + curr_sum):
            curr_sum = i
        else:
            curr_sum += i
        max_sum = max(max_sum, curr_sum)
    return max_sum

print(maxSubArray([5,4,-1,7,8]))