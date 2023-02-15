class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m = len(seats)
        n = len(seats[0])
        mat = []
        for row in seats:
            val = 0
            for c in row:
                val <<= 1
                if c == '#':
                    val |= 1
            mat.append(val)
        valid_bitmasks = []
        for bitmask in range(1 << n):
            flag = True
            used = False
            col = 1
            i = 0
            while i < n:
                if bitmask & col:
                    if used:
                        flag = False
                        break
                    used = True
                else:
                    used = False
                col <<= 1
                i += 1
            if flag:
                valid_bitmasks.append(bitmask)
        # print(len(valid_bitmasks))
        
        # row: current row
        # val: previous row bitmasks
        @cache
        def bt(row, val):
            # print(row, val)
            nonlocal mat, valid_bitmasks, m, n
            if row == m:
                return 0
            ans = 0
            for bitmask in valid_bitmasks:
                flag = True
                col = 1
                i = 0
                count = 0
                while i < n:
                    if bitmask & col:
                        count += 1
                        if (mat[row] & col) or (val & (col << 1)) or (val & (col >> 1)):
                            flag = False
                            break
                    col <<= 1
                    i += 1
                if flag:
                    ans = max(ans, count + bt(row + 1, bitmask))
            return ans
                
        return bt(0, 0)
        