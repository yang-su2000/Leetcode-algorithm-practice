class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(nums, k):
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
                return quick_select(l, k)
            elif len(l) + len(m) < k:
                return quick_select(r, k - len(l) - len(m))
            else:
                return pivot
        
        return quick_select(nums, k)