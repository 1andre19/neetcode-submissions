class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write_idx = 1

        for end in range(1,len(nums)):
            if nums[end] != nums[end - 1]:
                nums[write_idx] = nums[end]
                write_idx += 1
        
        return write_idx