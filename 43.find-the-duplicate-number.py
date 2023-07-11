# Can you solve the problem in linear runtime complexity?
# You must solve the problem without modifying the array nums and uses only constant extra space.

# Floyd's Cycle Detection

# Idea here is 2 phases
# Using slow and fast pointer to find the node before the beginning of the loop, which is somewhere slow and fast intersect
# Using another slow2 pointer to find the point of loop  


class Solution(object):
    def findDuplicate(self, nums):
        # always outside of the loop
        slow, fast = 0, 0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            # keep going until they intersect again
            if slow == fast:
                 break
            
        # phase 2
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow]
            if slow == slow2:
                return slow
        
        