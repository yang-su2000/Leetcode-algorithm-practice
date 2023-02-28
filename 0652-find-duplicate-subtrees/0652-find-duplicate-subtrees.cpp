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
    map<int, vector<TreeNode*>> m;
public:
    vector<TreeNode*> findDuplicateSubtrees(TreeNode* root) {
        get_depth(root);
        unordered_map<TreeNode*, TreeNode*> dup_m;
        vector<TreeNode*> ans;
        for (auto &p: m) {
            // cout << p.first << ":";
            // for (auto node: p.second) cout << node->val << ",";
            // cout << endl;
            map<tuple<int, TreeNode*, TreeNode*>, vector<TreeNode*>> level_m;
            for (TreeNode* node: p.second) {
                int val = node->val;
                TreeNode* left = nullptr;
                TreeNode* right = nullptr;
                if (!node->left);
                else if (dup_m.count(node->left)) left = dup_m[node->left];
                else continue;
                if (!node->right);
                else if (dup_m.count(node->right)) right = dup_m[node->right];
                else continue;
                level_m[{val, left, right}].push_back(node);
            }
            for (auto &t: level_m) {
                if (t.second.size() == 1) continue;
                TreeNode* target = t.second[0];
                for (TreeNode* node: t.second) dup_m[node] = target;
                // for (auto node: t.second) {
                //     debug(node);
                //     cout << " ";
                // }
                // cout << endl;
                ans.push_back(target);
            }
        }
        return ans;
    }
    
    int get_depth(TreeNode* node) {
        if (!node) return 0;
        int depth = 1 + max(get_depth(node->left), get_depth(node->right));
        m[depth].push_back(node);
        return depth;
    }
    
    void debug(TreeNode* node) {
        cout << "[" << node->val;
        if (node->left) {
            cout << ",";
            debug(node->left);
        }
        if (node->right) {
            cout << ",";
            debug(node->right);
        }
        cout << "]";
    }
};