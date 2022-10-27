class Solution:
    def canIWin(self, n: int, T: int) -> bool:
        if (1+n)*n < 2*T:
            return False
        # all 1's means that all numbers are available
        avail = (1 << n) - 1
        
        # stores seen states like dp
        @functools.cache
        def trace(a, t):
            for i in range(n):
                # need (condition 1) and (condition 2 or condition 3) for me to win
                # condition 1: current number i+1 is available
                # condition 2: using number i+1, I can win
                # condition 3: using number i+1, opponent would lose
                if a & (1 << i) and (t-(i+1) <= 0 or not trace(a ^ (1 << i), t-(i+1))):
                    return True
            return False
        
        return trace(avail, T)
            