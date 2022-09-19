class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for path in paths:
            ls = path.split()
            dir_name = ls[0]
            for i in range(1, len(ls)):
                file_name, content = ls[i].split('(')
                d[content].append(dir_name + '/' + file_name)
        return [val for val in d.values() if len(val) > 1]