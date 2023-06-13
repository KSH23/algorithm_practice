class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nonValIndex = 0

        for index, num in enumerate(nums):
            if num == val:
                continue
            
            if index != nonValIndex:
                nums[nonValIndex] = num
            nonValIndex += 1
        
        return nonValIndex
