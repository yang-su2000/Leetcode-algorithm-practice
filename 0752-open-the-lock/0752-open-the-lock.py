class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        d = {}
        s = set(deadends)
        if '0000' in s:
            return -1
        d['0000'] = 0
        cur = [(0, '0000')]
        while cur:
            dist, node = heappop(cur)
            if d[node] < dist:
                continue
            if node == target:
                return dist
            for i in range(4):
                for val in (-1, 1):
                    child = list(node)
                    if child[i] == '9' and val == 1:
                        child[i] = '0'
                    elif child[i] == '0' and val == -1:
                        child[i] = '9'
                    else:
                        child[i] = chr(ord(child[i]) + val)
                    child = ''.join(child)
                    if child in s:
                        continue
                    if child not in d or d[child] > dist + 1:
                        d[child] = dist + 1
                        heappush(cur, (dist + 1, child))
        return -1