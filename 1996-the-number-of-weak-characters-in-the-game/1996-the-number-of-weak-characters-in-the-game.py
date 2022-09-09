class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        max_attack = max([i[0] for i in properties])
        max_defs = [0 for _ in range(max_attack + 1)]
        for i in properties:
            max_defs[i[0]] = max(max_defs[i[0]], i[1])
        max_def = 0
        for i in range(max_attack, -1, -1):
            max_def = max(max_def, max_defs[i])
            max_defs[i] = max_def
        ans = 0
        for i in properties:
            if i[0] < max_attack and i[1] < max_defs[i[0] + 1]:
                ans += 1
        return ans