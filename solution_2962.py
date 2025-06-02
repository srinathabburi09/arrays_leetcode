class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        l = 0
        count = 0
        freq = 0
        n = len(nums)
        for r in range(n):
            if nums[r] == max_element:
                freq += 1
            
            while freq >= k:
                if nums[l] == max_element:
                    freq -= 1
                l += 1
            count += l

        return count
