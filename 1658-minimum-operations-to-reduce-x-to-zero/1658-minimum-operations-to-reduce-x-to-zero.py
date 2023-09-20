class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        psum = [0] * n
        psum[0] = nums[0]
        # edge case - only first
        if psum[0] == x:
            return 1
        ans = n + 1
        for i in range(1, n):
            psum[i] = psum[i-1] + nums[i]
            # edge case - only left
            if psum[i] == x:
                ans = min(ans, i + 1)
        ssum = [0] * n
        ssum[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            ssum[i] = ssum[i+1] + nums[i]
        for i in range(n-1, -1, -1):
            remain = x - ssum[i]
            op = n - i
            if remain < 0:
                continue
            elif remain == 0:
                ans = min(ans, op)
                continue
            else:
                l = 0
                r = i-1
                while l < r:
                    mid = (l + r) // 2
                    if psum[mid] < remain:
                        l = mid + 1
                    elif psum[mid] == remain:
                        l = mid
                        break
                    else:
                        r = mid - 1
                if psum[l] == remain:
                    op += l + 1
                    ans = min(ans, op)
        return ans if ans < n + 1 else -1