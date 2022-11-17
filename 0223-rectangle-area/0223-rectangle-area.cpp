class Solution {
public:
    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int ans = (C-A) * (D-B) + (G-E) * (H-F);
        if (C <= E or A >= G or B >= H or D <= F) return ans;
        vector <int> x {A, C, E, G};
        vector <int> y {B, D, F, H};
        sort(x.begin(), x.end());
        sort(y.begin(), y.end());
        ans -= (x[2] - x[1]) * (y[2] - y[1]);
        return ans;
    }
};