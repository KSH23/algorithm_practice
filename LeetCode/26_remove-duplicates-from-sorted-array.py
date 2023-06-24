class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1 # unique 숫자가 들어갈 자리
        unique_index = 0 # 다음 unique 숫자의 자리
        length = len(nums)

        while unique_index < length:
            # 다음 unique 숫자 탐색
            # 다음 unique 숫자는 현재 unique 숫자와 값이 다른 경우의 값
            while nums[unique_index] == nums[index - 1]:
                unique_index += 1 
                if unique_index == length:
                    return index

            # 현재 index의 숫자를 찾은 unique 숫자로 변경
            nums[index] = nums[unique_index]

            # while문의 한 사이클 기준은 현재 index의 위치
            index += 1

        return index
