class Solution {
public:
    bool validWordSquare(vector<string>& words) {
        int n = words.size();
        for (int i=0; i<n; i++) {
            string word = words[i];
            for (int j=0; j<word.length(); j++) {
                if (j >= n or i >= words[j].length() or word[j] != words[j][i]) return false;
            }
        }
        return true;
    }
};