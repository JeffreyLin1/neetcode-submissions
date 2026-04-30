class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j = len(numbers)-1
        i = 0
        while True:
            sum = numbers[i] + numbers[j]
            if sum == target:
                return [i + 1, j + 1]
            elif sum > target:
                j -= 1
            elif sum < target:
                i += 1
        