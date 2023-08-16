from sortedcontainers import SortedList

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        cur = SortedList(nums[:k])
        ans = [cur[-1]]
        for i in range(k, len(nums)):
            cur.remove(nums[i-k])
            cur.add(nums[i])
            ans.append(cur[-1])
        return ans