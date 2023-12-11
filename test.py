# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Input: nums = [3,3], target = 6
# Output: [0,1]


# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false



def is_subsequence(s1, s2):

    for i in range(len(list(s1))):
        for j in range(len(list(s2))):
            if s1[i] == s2[j]:
                i = i + 1
                if i == len(s1):
                    return True
            j = j + 1
    
    return False
s1 = "axc"
s2 = "ahbgdc"
print(is_subsequence(s1, s2))





def find_pair(nums, target):
    pass
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return i, j

    
            
    
    
# nums = [3,2,4]
# target = 9
# out = find_pair(nums, target)
# print(list(out))