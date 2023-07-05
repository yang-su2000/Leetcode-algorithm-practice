class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        nums.append(0)
        nums.append(0)
        zero_count = 0
        ls = []
        flag = True
        cur = 0
        ans = 0
        for i in nums:
            if i == 1:
                flag = True
                cur += 1
            elif flag:
                zero_count += 1
                flag = False
                ls.append(cur)
                cur = 0
            else:
                zero_count += 1
                flag = True
                for i in range(len(ls)):
                    if i < len(ls) - 1:
                        ans = max(ans, ls[i] + ls[i+1])
                    else:
                        ans = max(ans, ls[i])
                # print(ls)
                ls = []
                cur = 0
        if zero_count == 2:
            ans -= 1
        return ans