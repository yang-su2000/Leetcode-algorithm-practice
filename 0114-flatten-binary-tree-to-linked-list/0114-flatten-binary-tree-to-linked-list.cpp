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
    void flatten(TreeNode* root) {
        if (!root) return;
        flatten_(root);
    }
    
    // return rtail
    TreeNode* flatten_(TreeNode* node) {
        if (node->left) {
            TreeNode* rtail = flatten_(node->left);
            rtail->right = node->right;
            node->right = node->left;
            node->left = nullptr;
        }
        if (node->right) return flatten_(node->right);
        return node;
    }
};