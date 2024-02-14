class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a, b = [], []
        for i in nums:
            if i > 0:
                a.append(i)
            else:
                b.append(i)
        ans = []
        for x, y in zip(a, b):
            ans.append(x)
            ans.append(y)
        return ans