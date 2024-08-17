class Solution {
public:
    long long maximumValueSum(vector<vector<int>>& board) {
        long long m = board.size(), n = board[0].size();
        vector<vector<long long>> top_left(m, vector<long long>(n, LLONG_MIN));
        vector<vector<long long>> top_right(m, vector<long long>(n, LLONG_MIN));
        vector<vector<long long>> bot_left(m, vector<long long>(n, LLONG_MIN));
        vector<vector<long long>> bot_right(m, vector<long long>(n, LLONG_MIN));

        for (long long r = 0; r < m; ++r) {
            for (long long c = 0; c < n; ++c) {
                top_left[r][c] = board[r][c];
                if (r > 0)
                    top_left[r][c] = max((long long) top_left[r][c], top_left[r-1][c]);
                if (c > 0)
                    top_left[r][c] = max((long long) top_left[r][c], top_left[r][c-1]);
            }
        }

        for (long long r = m-1; r >= 0; --r) {
            for (long long c = 0; c < n; ++c) {
                bot_left[r][c] = board[r][c];
                if (r < m-1)
                    bot_left[r][c] = max((long long) bot_left[r][c], bot_left[r+1][c]);
                if (c > 0)
                    bot_left[r][c] = max((long long) bot_left[r][c], bot_left[r][c-1]);
            }
        }

        for (long long r = 0; r < m; ++r) {
            for (long long c = n-1; c >= 0; --c) {
                top_right[r][c] = board[r][c];
                if (r > 0)
                    top_right[r][c] = max((long long) top_right[r][c], top_right[r-1][c]);
                if (c < n-1)
                    top_right[r][c] = max((long long) top_right[r][c], top_right[r][c+1]);
            }
        }

        for (long long r = m-1; r >= 0; --r) {
            for (long long c = n-1; c >= 0; --c) {
                bot_right[r][c] = board[r][c];
                if (r < m-1)
                    bot_right[r][c] = max((long long) bot_right[r][c], bot_right[r+1][c]);
                if (c < n-1)
                    bot_right[r][c] = max((long long) bot_right[r][c], bot_right[r][c+1]);
            }
        }

        vector<vector<long long>> rmax(m, vector<long long>(n, LLONG_MIN));
        vector<vector<long long>> cmax(m, vector<long long>(n, LLONG_MIN));
        vector<vector<long long>> rmax2(m, vector<long long>(n, LLONG_MIN));
        vector<vector<long long>> cmax2(m, vector<long long>(n, LLONG_MIN));

        for (long long r = 0; r < m; ++r) {
            rmax[r][0] = board[r][0];
            for (long long c = 1; c < n; ++c)
                rmax[r][c] = max((long long) board[r][c], rmax[r][c-1]);
        }

        for (long long c = 0; c < n; ++c) {
            cmax[0][c] = board[0][c];
            for (long long r = 1; r < m; ++r)
                cmax[r][c] = max((long long) board[r][c], cmax[r-1][c]);
        }

        for (long long r = 0; r < m; ++r) {
            rmax2[r][n-1] = board[r][n-1];
            for (long long c = n-2; c >= 0; --c)
                rmax2[r][c] = max((long long) board[r][c], rmax2[r][c+1]);
        }

        for (long long c = 0; c < n; ++c) {
            cmax2[m-1][c] = board[m-1][c];
            for (long long r = m-2; r >= 0; --r)
                cmax2[r][c] = max((long long) board[r][c], cmax2[r+1][c]);
        }

        long long ans = LLONG_MIN;
        for (long long r = 1; r < m-1; ++r) {
            for (long long c = 1; c < n-1; ++c) {
                long long cur = LLONG_MIN;
                cur = max(cur, (long long) board[r][c] + top_left[r-1][c-1] + bot_right[r+1][c+1]);
                cur = max(cur, (long long) cmax2[r+1][c] + rmax2[r][c+1] + top_left[r-1][c-1]);
                cur = max(cur, (long long) rmax[r][c-1] + cmax2[r+1][c] + top_right[r-1][c+1]);
                cur = max(cur, (long long) board[r][c] + top_right[r-1][c+1] + bot_left[r+1][c-1]);
                cur = max(cur, (long long) cmax[r-1][c] + rmax2[r][c+1] + bot_left[r+1][c-1]);
                cur = max(cur, (long long) cmax[r-1][c] + rmax[r][c-1] + bot_right[r+1][c+1]);
                ans = max(ans, (long long) cur);
            }
        }

        return ans;
    }
};