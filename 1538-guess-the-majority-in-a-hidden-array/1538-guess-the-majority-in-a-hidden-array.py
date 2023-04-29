# """
# This is the ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares 4 different elements in the array
#	 # return 4 if the values of the 4 elements are the same (0 or 1).
#	 # return 2 if three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
#	 # return 0 : if two element have a value equal to 0 and two elements have a value equal to 1.
#    def query(self, a: int, b: int, c: int, d: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#

class Solution:
    def guessMajority(self, reader: 'ArrayReader') -> int:
        # n = reader.length()
        # flag = [True] * n
        # for i in range(0, n - 4, 4):
        #     a, b, c, d, e = i, i+1, i+2, i+3, i+4
        #     v1 = reader.query(a, b, c, d)
        #     v2 = reader.query(a, b, c, e)
        #     v3 = reader.query(a, b, d, e)
        #     v4 = reader.query(b, c, d, e)
        #     flag[i: i+5] = [flag[i]] * 5
        #     f = not flag[i]
        #     if v1 == 4 and v2 == 4:
        #         pass
        #     elif v1 == 4 and v2 == 2:
        #         flag[i+4] = f
        #     elif v1 == 2 and v2 == 4:
        #         flag[i+3] = f
        #     elif v1 == 2 and v2 == 2:
        #         if v3 == 0:
        #             flag[i+3: i+5] = [f] * 2
        #         elif v3 == 2:
        #             if v4 == 4:
        #                 flag[i+1: i+5] = [f] * 4
        #             elif v4 == 2:
        #                 flag[i+1] = f
        #             else:
        #                 print(1)
        #         else:
        #             flag[i+2] = f
        #     elif sorted([v1, v2]) == [0, 2]:
        #         if v3 == 0:
        #             if v4 == 2:
        #                 flag[i+1: i+4] = [f] * 3
        #             elif v4 == 0:
        #                 flag[i+1] = f
        #                 flag[i+4] = f
        #             else:
        #                 print(2)
        #         elif v3 == 2:
        #             flag[i+2] = f
        #             flag[i+4] = f
        #         else:
        #             print(3)
        #         if v1 == 0:
        #             flag[i+3] = not flag[i+3]
        #             flag[i+4] = not flag[i+4]
        #     else:
        #         assert v1 == 0 and v2 == 0
        #         if v3 == 0:
        #             flag[i+2: i+5] = [f] * 3
        #         elif v3 == 2:
        #             if v4 == 2:
        #                 flag[i+1] = f
        #                 flag[i+3: i+5] = [f] * 2
        #             elif v4 == 0:
        #                 flag[i+1: i+3] = [f] * 2
        #             else:
        #                 print(4)
        #         else:
        #             print(5)
        # total = sum(flag)
        # print(flag)
        n = reader.length()
        cnt_equal = 1
        cnt_differ = 0
        index_differ = -1

        def f(equal, i):
            nonlocal cnt_equal, cnt_differ, index_differ
            if equal:
                cnt_equal += 1
            else:
                cnt_differ += 1
                index_differ = i

        query0123 = reader.query(0, 1, 2, 3)
        query1234 = reader.query(1, 2, 3, 4)
        f(reader.query(1, 2, 3, 4) == query0123, 4)
        for i in range(5, n):
            f(reader.query(1, 2, 3, i) == query0123, i)
        f(reader.query(0, 2, 3, 4) == query1234, 1)
        f(reader.query(0, 1, 3, 4) == query1234, 2)
        f(reader.query(0, 1, 2, 4) == query1234, 3)
        return (0 if cnt_equal > cnt_differ else index_differ
                if cnt_differ > cnt_equal else -1)