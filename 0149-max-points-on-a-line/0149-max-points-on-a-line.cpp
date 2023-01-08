class Solution {
public:
    int maxPoints(vector<vector<int>>& points) {
        map<pair<double, double>, int> m;
        double a, b;
        for (vector<int> &i: points) {
            for (vector<int> &j: points) {
                if (j[0] - i[0] == 0) {
                    a = 1e8;
                    b = j[0];
                } else {
                    a = (j[1] * 1.f - i[1]) / (j[0] - i[0]);
                    b = j[1] - a * j[0];
                    a = roundf(a * 1000) / 1000;
                    b = roundf(b * 1000) / 1000;
                }
                // cout << a << " " << b << endl;
                m[{a, b}]++;
            }
        }
        int ans = 0;
        for (auto p: m) {
            // cout << p.first.first << " " << p.first.second << " " << p.second << endl;
            ans = max(ans, (1 + (int) (sqrt(1 + 4 * p.second))) / 2);
        }
        // cout << endl;
        return ans;
    }
};