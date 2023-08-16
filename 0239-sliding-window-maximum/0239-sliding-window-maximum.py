class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        cur = deque()
        for i in range(k):
            while cur and nums[cur[-1]] <= nums[i]:
                cur.pop()
            cur.append(i)
        ans = [nums[cur[0]]]
        for i in range(k, len(nums)):
            if cur and cur[0] == i - k:
                cur.popleft()
            while cur and nums[cur[-1]] <= nums[i]:
                cur.pop()
            cur.append(i)
            ans.append(nums[cur[0]])
        return ans