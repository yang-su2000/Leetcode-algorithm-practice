class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        ls = []
        n = len(plantTime)
        for i in range(n):
            ls.append((growTime[i], plantTime[i]))
        ls.sort(reverse=True)
        ans = 0
        psum = 0
        for gt, pt in ls:
            psum += pt
            ans = max(ans, psum + gt)
        return ans