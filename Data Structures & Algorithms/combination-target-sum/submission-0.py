class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        
        def backtrack(currSum, curr, idx):
            if currSum > target:
                return
            if currSum == target:
                res.append(list(curr))

            for i in range(idx, len(nums)):
                curr.append(nums[i])
                currSum += nums[i]
                backtrack(currSum, curr, idx)
                curr.pop()
                currSum -= nums[i]
                idx += 1
        
        backtrack(0, [], 0)
        return res
