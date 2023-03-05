class Solution:
    def getp(self, ret, num):
        for i in range(2, int(sqrt(num)) + 1):
            done = False
            while num % i == 0:
                if not done:
                    ret[i] += 1
                    done = True
                num //= i
        if num > 1:
            ret[num] += 1
    
    def findValidSplit(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return -1
        mval = max(nums)
        l = [0] * (mval + 1)
        self.getp(l, nums[0])
        r = [0] * (mval + 1)
        for i in range(1, n):
            self.getp(r, nums[i])
        done = True
        count = 0
        for i in range(mval + 1):
            if l[i] and r[i]:
                done = False
                count += r[i]
        if done:
            return 0
        # print(l, r)
        for idx in range(1, n - 1):
            num = nums[idx]
            for i in range(2, int(sqrt(num)) + 1):
                done = False
                while num % i == 0:
                    if not done:
                        if l[i] == 0:
                            count += r[i] - 1
                            l[i] = 1
                        else:
                            count -= 1
                        done = True
                    num //= i
            if num > 1:
                if l[num] == 0:
                    count += r[num] - 1
                    l[num] = 1
                else:
                    count -= 1
            # print(l, r)
            if not count:
                return idx
        return -1
            