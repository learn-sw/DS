# Problem:
# Given an unsorted list of integers, return all combinations of 4 integers such that a + b + c = z where a, b, c, and z are all integers in the given list. Each element of the list may only be used once in each combination. Note: The interviewer discouraged sorting the inputted list.

# Example:

# Input: [9, 3, 2, 1, 6]
# Output: [1, 2, 3, 6], [1, 2, 6, 9]


def target_sum(nums):
    # nums: list

    if len(nums) < 4:
        return []
    dict_num = {}
    result = []
    for i in range(len(nums)):
        if nums[i] not in dict_num:
            dict_num[nums[i]] = i


    for i in range(0,len(nums)-2):
        for j in range(i+1,len(nums)-1):
            sum =  nums[i]+nums[j]+nums[j+1]
            if sum in dict_num:
                temp_list = sorted([nums[i],nums[j], nums[j+1],sum])
                #temp_list.append(sum)
                result.append(temp_list)

    return result

nums = [9, 3, 2, 1, 6]
print(target_sum(nums))