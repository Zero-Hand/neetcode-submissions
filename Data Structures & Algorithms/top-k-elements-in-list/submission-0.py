class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        x = []
        bucket = [[] for _ in range(len(nums)+1) ]

        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        for nums, freq in seen.items():
          bucket[freq].append(nums)
        
        
        for freq in range(len(bucket) -1 , 0 , -1):
          for num in bucket[freq]:
            x.append(num)
            if len(x) == k:
              return x 
        