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
    int ans = INT_MIN;
public:
    int maxPathSum(TreeNode* root) {
        rec(root);
        return ans;
    }
    
    // return path sum with root as one end
    int rec(TreeNode* root) {
        int l = 0, r = 0;
        if (root->left) l = rec(root->left);
        if (root->right) r = rec(root->right);
        int ret = max(0, max(l, r)) + root->val;
        ans = max(ans, max(ret, l + r + root->val));
        return ret;
    }
};