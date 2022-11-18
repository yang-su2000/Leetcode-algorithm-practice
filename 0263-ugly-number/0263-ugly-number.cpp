class Solution {
public:
    bool isUgly(int n) {
        if (n < 1) return false;
        int ls[3] = {2, 3, 5};
        bool done = false;
        while (n != 1 and !done) {
            done = true;
            for (int &p:ls) {
                if (n % p == 0) {
                    n /= p;
                    done = false;
                }
            }
        }
        if (done) return false;
        return true;
    }
};