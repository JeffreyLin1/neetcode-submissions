class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        totalpre = 1
        totalpost = 1
        for i, j in enumerate(nums):
            totalpre *= j
            totalpost *= nums[-1-i]
            prefix.append(totalpre)
            postfix.append(totalpost)
        postfix.reverse()
        print(prefix)
        output = []
        output.append(postfix[1])
        for i in range(1, len(nums)-1):
            output.append(prefix[i-1] * postfix[i+1])
        output.append(prefix[-2])
        return output
