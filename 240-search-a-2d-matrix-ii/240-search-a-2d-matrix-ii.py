class Solution:
    def searchMatrix(self, m: List[List[int]], target: int) -> bool:
        return self.search(m, target, 0, len(m) - 1, 0, len(m[0]) - 1)
    
    def search(self, m, target, li, ri, lj, rj):
        if li > ri or lj > rj:
            return False
        if li == ri and lj == rj:
            return m[li][lj] == target
        midi = (li + ri) // 2
        midj = (lj + rj) // 2
        cur = m[midi][midj]
        # print(li, ri, lj, rj, ':', midi, midj, cur)
        if cur == target:
            return True
        elif cur > target:
            if self.search(m, target, li, midi, lj, midj) or \
                self.search(m, target, li, midi-1, midj, midj) or \
                self.search(m, target, midi, midi, lj, midj-1):
                return True
        else:
            if self.search(m, target, midi+1, ri, midj+1, rj) or \
                self.search(m, target, midi, midi, midj+1, rj) or \
                self.search(m, target, midi+1, ri, midj, midj):
                return True
        return self.search(m, target, li, midi-1, midj+1, rj) or \
            self.search(m, target, midi+1, ri, lj, midj-1)