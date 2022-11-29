class Solution {
public:
    bool sub(string &s, int l, int r, bool magic) {
        while (l < r) {
            if (s[l] != s[r]) {
                if (magic) return sub(s, l+1, r, false) or sub(s, l, r-1, false);
                else return false;
            } else {l++, r--;}
        }
        return true;
    }
    
    bool validPalindrome(string s) {
        return sub(s, 0, s.length()-1, true);
    }
};