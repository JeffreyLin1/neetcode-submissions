class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            j = len(numbers)-1
            while i != j:
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
                j -= 1
        