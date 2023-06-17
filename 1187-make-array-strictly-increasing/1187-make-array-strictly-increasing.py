class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        # arr3 = []
        # for i in arr2:
        #     if arr3 and arr3[-1] == i:
        #         continue
        #     else:
        #         arr3.append(i)
        # arr2 = arr3
        # print(arr2)
        
        @cache
        def dfs(i, prev):
            if i == len(arr1):
                return 0
            cost = inf
            if arr1[i] > prev:
                cost = dfs(i+1, arr1[i])
            idx = bisect.bisect_right(arr2, prev)
            if idx < len(arr2):
                cost = min(cost, 1 + dfs(i+1, arr2[idx]))
            return cost
        
        ans = dfs(0, -1)
        return ans if ans != inf else -1