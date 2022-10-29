class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        ans = []
        arr.sort()
        min_val = float('inf')
        for i in range(len(arr) - 1):
            val = arr[i+1] - arr[i]
            if val < min_val:
                ans = [[arr[i], arr[i+1]]]
                min_val = val
            elif val == min_val:
                ans.append([arr[i], arr[i+1]])
        return ans