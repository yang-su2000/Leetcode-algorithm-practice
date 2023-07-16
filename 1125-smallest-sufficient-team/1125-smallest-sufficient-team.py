class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(req_skills)
        d = {req_skills[i]: i for i in range(n)}
        ls = []
        for skills in people:
            val = 0
            for skill in skills:
                val |= (1 << d[skill])
            ls.append(val)
        # print(ls)
        m = len(ls)
        dp = [(1 << m) - 1] * (1 << n) # skill_mask -> people_mask
        dp[0] = 0
        for skill_mask in range(1, 1 << n): # 2**16
            for i, p in enumerate(ls): # 60
                skill_mask2 = skill_mask & ~p
                people_mask2 = dp[skill_mask2] | (1 << i)
                if skill_mask2 != skill_mask and people_mask2.bit_count() < dp[skill_mask].bit_count():
                    dp[skill_mask] = people_mask2
            # print(dp)
        res = dp[(1 << n) - 1]
        ans = []
        for i in range(m):
            if res & (1 << i):
                ans.append(i)
        return ans