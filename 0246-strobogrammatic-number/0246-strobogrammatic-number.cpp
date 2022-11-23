class Solution {
public:
    bool isStrobogrammatic(string num) {
        map<char, char> m {{'0', '0'}, {'1', '1'}, {'6', '9'}, {'8', '8'}, {'9', '6'}};
        string num2 = "";
        for (auto &c: num) {
            if (!m.count(c)) return false;
            num2 += m[c];
        }
        reverse(num.begin(), num.end());
        return num == num2;
    }
};