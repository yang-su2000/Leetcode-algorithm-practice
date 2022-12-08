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
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        return getSequence(root1) == getSequence(root2);
    }
    
    vector<int> getSequence(TreeNode* root) {
        vector<int> ret;
        rec(root, ret);
        return ret;
    }
    
    void rec(TreeNode* root, vector<int>& ret) {
        if (!root->left and !root->right) {
            ret.emplace_back(root->val);
            return;
        }
        if (root->left) rec(root->left, ret);
        if (root->right) rec(root->right, ret);
    }
};