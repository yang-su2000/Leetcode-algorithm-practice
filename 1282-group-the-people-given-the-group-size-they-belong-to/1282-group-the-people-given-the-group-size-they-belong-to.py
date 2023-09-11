class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        for i, val in enumerate(groupSizes):
            d[val].append(i)
        ans = []
        for val, ls in d.items():
            for i in range(0, len(ls), val):
                ans.append(ls[i: i + val])
        return ans
        