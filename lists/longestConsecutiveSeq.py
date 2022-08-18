def longestConsecutive(self, nums: List[int]) -> int:
        
       
        # easy solution: with sorting
        if not nums: return 0
        if len(nums) == 1: return 1
#         nums.sort()
#         print(nums)
        
#         longest = streak = 1
        
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i - 1] + 1:
#                 streak += 1
#                 longest = max(longest, streak)
#             elif nums[i] == nums[i - 1]:
#                 continue
#             else:
#                 streak = 1
            
            
#         return longest
    
        ## Better solution O(n)
        longest = 0
        numset = set(nums)
        
        for num in numset:
            
            if num - 1 not in numset:
                streak = 1
                nextnum = num + 1
                while nextnum in numset:
                    streak += 1
                    nextnum += 1
                longest = max(longest, streak)
                
        return longest
