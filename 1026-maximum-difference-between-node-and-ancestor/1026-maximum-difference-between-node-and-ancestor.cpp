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
class Solution {
public:
    int maxAncestorDiff(TreeNode* root) {
        int ans = 0;
        rec(root, ans);
        return ans;
    }
    
    // minval, maxval
    pair<int, int> rec(TreeNode* root, int &ans) {
        int minval = root->val;
        int maxval = root->val;
        if (root->left) {
            auto p = rec(root->left, ans);
            minval = min(minval, p.first);
            maxval = max(maxval, p.second);
        }
        if (root->right) {
            auto p = rec(root->right, ans);
            minval = min(minval, p.first);
            maxval = max(maxval, p.second);
        }
        ans = max(ans, max(abs(root->val - minval), abs(root->val - maxval)));
        return {minval, maxval};
    }
};