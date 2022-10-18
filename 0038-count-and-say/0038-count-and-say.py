class Solution:
    def countAndSay(self, n: int) -> str:
        ans = '1'
        for i in range(1, n):
            nxt = ''
            cur = ans[0]
            count = 1
            for j in range(1, len(ans)):
                if ans[j] == cur:
                    count += 1
                else:
                    nxt += str(count) + cur
                    cur = ans[j]
                    count = 1
            ans = nxt + str(count) + cur
            # print(ans)
        return ans