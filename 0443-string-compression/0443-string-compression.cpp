class Solution {
public:
    int compress(vector<char>& chars) {
        int l = 1;
        int l2 = 0;
        int r = chars.size();
        char c = chars[0];
        int count = 1;
        while (l < r) {
            if (chars[l] == c) count++;
            else {
                chars[l2++] = c;
                if (count > 1) {
                    for (char c2: to_string(count)) chars[l2++] = c2;
                }
                c = chars[l];
                count = 1;
            }
            l++;
        }
        chars[l2++] = c;
        if (count > 1) {
            for (char c2: to_string(count)) chars[l2++] = c2;
        }
        return l2;
    }
};