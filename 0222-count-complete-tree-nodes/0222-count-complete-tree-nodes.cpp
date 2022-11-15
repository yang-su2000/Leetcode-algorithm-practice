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
    int countNodes(TreeNode* root) {
        stack<TreeNode*> s;
        s.push(root);
        int ans=0;
        while (!s.empty()) {
            TreeNode* node = s.top();
            s.pop();
            if (node) {
                ans++;
                s.push(node->left);
                s.push(node->right);
            }
        }
        return ans;
    }
};