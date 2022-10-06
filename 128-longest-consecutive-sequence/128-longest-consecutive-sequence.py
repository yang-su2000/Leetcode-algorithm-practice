class Union:
    def __init__(self):
        self.parents = {}
        self.size = {}
        
    def find(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]
    
    def union(self, i, j):
        i, j = self.find(i), self.find(j)
        if self.size[i] >= self.size[j]:
            self.size[i] += self.size[j]
            self.parents[j] = i
        else:
            self.size[j] += self.size[i]
            self.parents[i] = j

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        U = Union()
        for i in nums:
            if i in U.parents:
                continue
            U.parents[i] = i
            U.size[i] = 1
            if i+1 in U.parents:
                U.union(i, i+1)
            if i-1 in U.parents:
                U.union(i, i-1)
        return max(U.size.values())