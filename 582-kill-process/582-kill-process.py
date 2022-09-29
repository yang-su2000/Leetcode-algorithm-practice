class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        d = defaultdict(list)
        for i in range(len(pid)):
            parent, child = ppid[i], pid[i]
            d[parent].append(child)
        visited = set()
        q = [kill]
        while q:
            i = q.pop()
            if i not in visited:
                visited.add(i)
                for child in d[i]:
                    q.append(child)
        return list(visited)