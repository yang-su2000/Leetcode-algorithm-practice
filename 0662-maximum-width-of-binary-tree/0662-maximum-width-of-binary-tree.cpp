/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#define ll long long

class Solution {
public:
    int widthOfBinaryTree(TreeNode* root) {
        int ans = 0;
        vector<pair<ll, TreeNode*>> v;
        v.push_back({0, root});
        while (!v.empty()) {
            vector<pair<ll, TreeNode*>> v2;
            ll lval = LLONG_MAX;
            ll rval = 0;
            for (auto &p: v) {
                ll val = p.first;
                TreeNode* node = p.second;
                lval = min(lval, val);
                rval = max(rval, val);
                if (node->left) v2.push_back({val * 2, node->left});
                if (node->right) v2.push_back({val * 2 + 1, node->right});
            }
            for (auto &p: v2) p.first -= lval;
            ans = max(ans, (int) (rval - lval));
            swap(v, v2);
        }
        return ans + 1;
    }
};