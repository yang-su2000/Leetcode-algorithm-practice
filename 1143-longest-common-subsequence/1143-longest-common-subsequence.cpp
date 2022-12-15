class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int n1 = text1.length();
        int n2 = text2.length();
        int i, j, val;
        vector<int> prev(n2);
        vector<int> cur(n2);
        for (i=0; i<n1; i++) {
            for (j=0; j<n2; j++) {
                val = 0;
                if (i>0) val = max(val, prev[j]);
                if (j>0) val = max(val, cur[j-1]);
                if (text1[i] == text2[j]) {
                    if (i>0 and j>0) val = max(val, prev[j-1]+1);
                    else val = max(val, 1);
                }
                cur[j] = val;
                // printf("%d ", cur);
            }
            prev = cur;
            // printf("\n");
        }
        return prev[n2-1];
    }
};