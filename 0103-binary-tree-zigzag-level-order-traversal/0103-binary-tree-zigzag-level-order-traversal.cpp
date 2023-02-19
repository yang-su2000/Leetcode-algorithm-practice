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
    vector<vector<int>> win;
public:
    void rec(TreeNode* root, int lvl) {
        if (!root) return;
        if (win.size()==lvl) {
            win.push_back({root->val});
        } else win[lvl].push_back({root->val});
        rec(root->left, lvl+1);
        rec(root->right, lvl+1);
    }
    
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        rec(root, 0);
        for (int i=1; i<win.size(); i+=2) reverse(win[i].begin(), win[i].end());
        return win;
    }
};