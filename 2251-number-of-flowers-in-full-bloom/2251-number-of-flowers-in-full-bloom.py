class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        d = defaultdict(int)
        for a, b in flowers:
            d[a] += 1
            d[b+1] -= 1
        ls = []
        total_count = 0
        for time, count in sorted(d.items()):
            total_count += count
            ls.append((time, total_count))
        # print(ls)
        n = len(people)
        ps = sorted((people[i], i) for i in range(n))
        ans = [-1] * n
        li = 0
        cur = 0
        for pi in range(n):
            time, i = ps[pi]
            while li < len(ls) and ls[li][0] <= time:
                cur = ls[li][1]
                li += 1
            ans[i] = cur
        return ans