class Solution {
public:
    int shortestWordDistance(vector<string>& wordsDict, string word1, string word2) {
        int p1 = -1;
        int p2 = -1;
        int ans = INT_MAX;
        if (word1 == word2) {
            for (int i=0; i<wordsDict.size(); i++) {
                string s = wordsDict[i];
                if (s == word1) {
                    if (p1 == -1) p1 = i;
                    else {
                        ans = min(ans, i - p1);
                        p1 = i;
                    }
                }
            }
            return ans;
        }
        for (int i=0; i<wordsDict.size(); i++) {
            string s = wordsDict[i];
            if (s == word1) p1 = i;
            else if (s == word2) p2 = i;
            if (p1 != -1 and p2 != -1) ans = min(ans, abs(p1 - p2));
        }
        return ans;
    }
};