# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, arr: 'MountainArray') -> int:

        def findMax(l, r):
            while l < r:
                mid = (l + r) // 2
                ls = [arr.get(mid), arr.get(mid+1)]
                if ls[0] < ls[1]:
                    l = mid + 1
                else:
                    r = mid
            return l
        
        def search(l, r, inc=True):
            while l < r:
                mid = (l + r) // 2
                val = arr.get(mid)
                if val == target:
                    return mid
                elif val < target:
                    if inc:
                        l = mid + 1
                    else:
                        r = mid - 1
                else:
                    if inc:
                        r = mid - 1
                    else:
                        l = mid + 1
            if arr.get(l) == target:
                return l
            return -1
            
        n = arr.length()
        mid = findMax(0, n-1)
        # print(mid)
        ans = search(0, mid, inc=True)
        if ans != -1:
            return ans
        return search(mid, n-1, inc=False)
            