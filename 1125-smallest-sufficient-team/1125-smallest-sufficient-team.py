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
        n = (1 << n)
        m = len(ls)
        dp = [[None] * n for _ in range(m + 1)] # (cur_people, skills) -> (size, set_people)
        dp[0][0] = (0, 0)
        for i in range(m):
            skill = ls[i]
            for j in range(n):
                if dp[i][j] is None:
                    continue
                val, res = dp[i][j]
                # pick
                skill2 = (j | skill)
                if dp[i+1][skill2] is None or val + 1 < dp[i+1][skill2][0]:
                    dp[i+1][skill2] = (val + 1, res | (1 << i))
                # not pick
                if dp[i+1][j] is None or val < dp[i+1][j][0]:
                    dp[i+1][j] = (val, res)
        # for i in range(m + 1):
        #     print(i, dp[i])
        res = dp[m][n - 1][1]
        ret = []
        for i in range(m):
            if res & (1 << i):
                ret.append(i)
        return ret