class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i = 0
        n = len(sandwiches)
        while students and i < n:
            students2 = []
            for s in students:
                if i < n and s == sandwiches[i]:
                    i += 1
                else:
                    students2.append(s)
            if len(students2) == len(students):
                return len(students)
            students = students2
        return len(students)