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
    map<int, TreeNode*> M;
    vector<int> ret;
public:
    // due to uniqueness, this actually connects child and parent as a graph
    void findParents(TreeNode* root) {
        if (root->left) {
            M[root->left->val] = root;
            findParents(root->left);
        }
        if (root->right) {
            M[root->right->val] = root;
            findParents(root->right);
        }
    }

    void dfs(TreeNode* cur, int remain) {
        if (cur->val == -1) return;
        int curVal = cur->val;
        cur->val = -1; // denote discovered
        if (remain == 0) {
            ret.emplace_back(curVal);
            return;
        }
        if (cur->left) dfs(cur->left, remain-1); // go left child
        if (cur->right) dfs(cur->right, remain-1); // go right child
        if (M[curVal]) dfs(M[curVal], remain-1); // go parent
    }

    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        findParents(root); // treat the tree as a graph, centered at target
        dfs(target, k);
        return ret;
    }
};