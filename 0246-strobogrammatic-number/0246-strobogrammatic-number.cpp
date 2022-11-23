class Solution {
public:
    bool isStrobogrammatic(string num) {
        int l=0, r=num.size()-1;
        while (l<=r) {
            if ((num[l]=='8' and num[r]=='8') or (num[l]=='6' and num[r]=='9') or (num[l]=='0' and num[r]=='0') or (num[l]=='1' and num[r]=='1') or (num[l]=='9' and num[r]=='6')) {l++, r--;}
            else return false;
        }
        return true;
    }
};