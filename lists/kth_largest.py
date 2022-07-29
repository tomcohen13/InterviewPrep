def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # Easy solution: with sorting
        
        #print(f"Finding the {k}th largest here:", nums)
        mid = nums[-k]
        #print(f"Picked {mid} as pivot")
        smaller = []
        larger = []
        equal = []
        
        # divide nums into smaller and larger than middle
        for num in nums:
            if num < mid:
                smaller.append(num)
            elif num == mid:
                equal.append(num)
            else:
                larger.append(num)
        
        # three options:
        
        # 1) we've found the kth largest:
        if len(larger) == k - 1 or (not larger and not smaller):
            #print("Found it!")
            return mid
        
        # 2) Kth largest is in larger elements
        if len(larger) > k - 1:
            return self.findKthLargest(larger, k)
        
        # 3) Kth largest is in smaller elements
        else:
            return self.findKthLargest(smaller + equal, k - len(larger))
            
