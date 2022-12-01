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
public:    
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        stack<TreeNode*> s;
        s.push(root);
        // node->val, val = 0 (unfound), 1 (found p), 2 (found q), 3 (found both)
        unordered_map<TreeNode*, int> m; 
        while (!s.empty()) {
            TreeNode* node = s.top();
            if (!node) {
                s.pop();
                continue;
            }
            if (!m.count(node)) {
                m[node] = 0;
                s.push(node->left);
                s.push(node->right);
                continue;
            }
            int val = m[node->left] + m[node->right];
            if (node == p) val += 1;
            if (node == q) val += 2;
            if (val == 3) return node;
            // m.erase(node->left);
            // m.erase(node->right);
            m[node] = val;
            s.pop();
        }
        return nullptr;
    }
};