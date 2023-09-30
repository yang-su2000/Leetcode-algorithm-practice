class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        lo = [0] * n
        lo[0] = nums[0]
        for i in range(1, n):
            lo[i] = min(lo[i-1], nums[i])
        st = []
        for i in range(n - 1, -1, -1):
            if nums[i] <= lo[i]:
                continue
            while st and st[-1] <= lo[i]:
                st.pop()
            if st and st[-1] < nums[i]:
                return True
            st.append(nums[i])
        return False