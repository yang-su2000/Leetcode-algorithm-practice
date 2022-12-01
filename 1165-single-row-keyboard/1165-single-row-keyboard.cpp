class Solution {
public:
    int calculateTime(string keyboard, string word) {
        unordered_map<char, int> m;
        for (int i=0; i<keyboard.length(); i++) m[keyboard[i]] = i;
        int ans = 0;
        int p = 0;
        for (char &c: word) {
            ans += abs(m[c] - p);
            p = m[c];
        }
        return ans;
    }
};