class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int n1 = s1.length();
        int n2 = s2.length();
        if (n1 > n2) return false;
        vector<int> v1(26);
        for (char c: s1) v1[c-'a']++;
        vector<int> v2(26);
        for (int i=0; i<n1; i++) v2[s2[i]-'a']++;
        if (v1 == v2) return true;
        for (int i=n1; i<n2; i++) {
            v2[s2[i-n1]-'a']--;
            v2[s2[i]-'a']++;
            if (v1 == v2) return true;
        }
        return false;
    }
};