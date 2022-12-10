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
    long ans = 0;
    long sum = 0;
    int modulo = 1e9+7;
public:
    int maxProduct(TreeNode* root) {
        sum = getSum(root);
        rec(root);
        return ans % modulo;
    }
    
    long rec(TreeNode* root) {
        if (!root) return 0;
        long mySum = root->val + rec(root->left) + rec(root->right);
        ans = max(ans, mySum * (sum - mySum));
        return mySum;
    }
    
    long getSum(TreeNode* root) {
        if (!root) return 0;
        return root->val + getSum(root->left) + getSum(root->right);
    }
};