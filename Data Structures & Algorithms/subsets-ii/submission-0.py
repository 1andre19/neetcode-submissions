class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(curr, idx):
            res.append(list(curr))

            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                curr.append(nums[i])
                backtrack(curr, i + 1)
                curr.pop()
        
        backtrack([], 0)
        return res