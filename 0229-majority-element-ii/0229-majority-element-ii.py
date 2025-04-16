class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority_1 = None
        count_1 = 0

        majority_2 = None
        count_2 = 0

        for i in range(len(nums)):
            if nums[i] == majority_1:
                count_1 += 1
            elif nums[i] == majority_2:
                count_2 += 1
            elif count_1 == 0:
                majority_1 = nums[i]
                count_1 = 1
            elif count_2 == 0:
                majority_2 = nums[i]
                count_2 = 1
            else:
                count_1 -= 1
                count_2 -= 1

        result = []
        freq_1, freq_2 = 0, 0
        for i in range(len(nums)):
            if majority_1 == nums[i]:
                freq_1 += 1
            elif majority_2 == nums[i]:
                freq_2 += 1

        if freq_1 > len(nums) // 3:
            result.append(majority_1)
        if freq_2 > len(nums) // 3:
            result.append(majority_2)

        return result

            

            

            