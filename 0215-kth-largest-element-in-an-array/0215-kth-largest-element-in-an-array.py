class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pivot = random.choice(nums)
        l, m, r = [], [], []
        for i in nums:
            if i > pivot:
                l.append(i)
            elif i == pivot:
                m.append(i)
            else:
                r.append(i)
        if k <= len(l):
            return self.findKthLargest(l, k)
        elif k <= len(l) + len(m):
            return pivot
        else:
            return self.findKthLargest(r, k - len(l) - len(m))