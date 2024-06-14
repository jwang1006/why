class Solution:
    def longestConsecutive(self, nums) -> int:
        if len(nums)==0:
            return 0
        print(nums[0])
        nums.sort()
        best = 0
        streak = 1
        last = nums[0]
        for n in nums:
            if n == last+1:
                streak+=1
            elif streak>best:
                best = streak
                streak = 1
            last = n
        if streak>best:
            best = streak
        return best

bob = Solution()
bob.longestConsecutive([3, 5, 4, 2])