class Solution {
public:
    int climbStairs(int n) {
        int l1 = 0;
        int l2 = 1;
        while (n) {
            int l1_next = l2;
            l2 += l1;
            l1 = l1_next;
            n--;
        }
        return l2;
    }
};