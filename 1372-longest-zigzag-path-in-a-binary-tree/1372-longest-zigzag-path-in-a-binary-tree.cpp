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
#define pi pair<int, int>

class Solution {
    int ans = 0;
public:
    int longestZigZag(TreeNode* root) {
        pi val = rec(root);
        return ans;
    }
    
    pi rec(TreeNode* node) {
        if (!node) return {-1, -1};
        pi l = rec(node->left);
        pi r = rec(node->right);
        int a = 1 + l.second;
        int b = 1 + r.first;
        ans = max(ans, max(a, b));
        return {a, b};
    }
};