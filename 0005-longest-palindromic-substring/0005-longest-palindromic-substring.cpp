class Solution {
public:
    string longestPalindrome(string s) {
        int l=0;
        int n=s.size();
        int j=0;
        int start=0;
        int end=0;
        for (int i=0; i<n-l; i++){
            j=0;
            while (i>=j && i+j+1<n) {
                if (s[i-j]!=s[i+j+1]) break;
                j++;
            }
            if (j>=l) {
                l=j;
                start=i-j+1;
                end=2*j;
            }
            j=1;
            while (i>=j && i+j<n) {
                if (s[i-j]!=s[i+j]) break;
                j++;
            }
            if (j>l) {
                l=j;
                start=i-j+1;
                end=2*j-1;
            }
        }
        return s.substr(start,end);
    }
};