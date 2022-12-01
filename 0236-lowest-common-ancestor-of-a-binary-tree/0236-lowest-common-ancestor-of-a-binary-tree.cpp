/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
    TreeNode* ans = NULL;
    int pv, qv;
public:
    // 0: unfound, 1: found p, 2: found q, 3: found both
    int rec(TreeNode* root) {
        if (!root) return 0;
        if (ans) return 3;
        int ret = rec(root->left) + rec(root->right);
        if (ans) return 3;
        if (root->val == pv) ret += 1;
        if (root->val == qv) ret += 2;
        if (ret == 3) ans = root;
        // cout << root->val << "," << ret << endl;
        return ret;
    }
    
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        pv = p->val;
        qv = q->val;
        rec(root);
        return ans;
    }
};