class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index1, index2 = 0, 0
        len1 = len(nums1)

        while index1 < len1 and index2 < n:
            if index1 >= m:
                nums1[index1:] = nums2[index2:]
                return
            
            num1, num2 = nums1[index1], nums2[index2]
            if num1 <= num2:
                index1 += 1
                continue
            
            nums1[index1 + 1: len1] = nums1[index1: len1 - 1]
            nums1[index1] = num2
            index1 += 1
            index2 += 1
            m += 1 # merge 시작점 갱신
