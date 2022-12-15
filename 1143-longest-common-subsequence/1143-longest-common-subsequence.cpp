class Trie {
    bool tail;
    unordered_map<char, Trie*> m;
    
    Trie(): tail {false} {}
    
    void find(string &s, int i) {
        if (i == s.length()) {
            tail = true;
            return;
        }
        m[s[i]]->find(s, i+1);
    }
};

class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int n1 = text1.length();
        int n2 = text2.length();
        int i, j, cur;
        vector<vector<int>> dp(n1, vector<int>(n2));
        for (i=0; i<n1; i++) {
            for (j=0; j<n2; j++) {
                cur = 0;
                if (i>0) cur = max(cur, dp[i-1][j]);
                if (j>0) cur = max(cur, dp[i][j-1]);
                if (text1[i] == text2[j]) {
                    if (i>0 and j>0) cur = max(cur, dp[i-1][j-1]+1);
                    else cur = max(cur, 1);
                }
                dp[i][j] = cur;
                // printf("%d ", cur);
            }
            // printf("\n");
        }
        return dp[n1-1][n2-1];
    }
};