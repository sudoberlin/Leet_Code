# problem - Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

#brute force way
class Solution:
    def twosums(self,nums,target):
        for i in range (len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

# More efficient way
class Solution :
    def twosums(self, nums, target):
        # make a dictionary to store the value
        dict = { }
        for i in range (len(nums)):
            required = target - nums[i]
            if required in dict:
                return[dict[required],i]
            dict[nums[i]] = i

# driver code to execute


nums = [1, 2, 3, 45, 55]
target = Solution()
print(target.twosums(nums, 4))


