class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        n = len(damage)
        hp = [0] * n
        for i in range(n):
            hp[i] = ceil(health[i] / power)
        dh = sorted([(damage[i] / hp[i], i) for i in range(n)], reverse=True)
        # print(hp, dh)
        ds = sum(damage)
        ans = 0
        for _, i in dh:
            ans += ds * hp[i]
            ds -= damage[i]
        return ans


# inclusion-exclusion (_ _ _ _ _ : x1 _ _ _ _ vs. _ x1 _ _ _ -> x1 x2 _ _ _ vs. x2 x1 _ _ _)
# damage -> di, rounds -> ri
# sum_val == _ _ _
# ans_left = r1 * (sum_val + d1 + d2) + r2 * (sum_val + d2) = 
# ans_right = r2 * (sum_val + d1 + d2) + r1 * (sum_val + d1) = 

# ans_left = r1 * d2
# ans_right = r2 * d1
# r1 * d2 ~><= r2 * d1
# d2 / r2 ~><= d1 / r1
