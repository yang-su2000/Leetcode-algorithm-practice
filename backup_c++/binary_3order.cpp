/**
 * struct TreeNode {
 *	int val;
 *	struct TreeNode *left;
 *	struct TreeNode *right;
 * };
 */

class Solution {
public:
    /**
     * 
     * @param root TreeNode类 the root of binary tree
     * @return int整型vector<vector<>>
     */
    vector<int> preorder1(TreeNode* root) {
        vector<int> ret;
        stack<TreeNode*> s;
        s.push(root);
        while (!s.empty()){
            TreeNode* cur=s.top();
            s.pop();
            if (cur) {
                ret.push_back(cur->val);
                s.push(cur->right);
                s.push(cur->left);
            }
        }
        return ret;
    }
    
    vector<int> inorder1(TreeNode* root) {
        vector<int> ret;
        stack<pair<TreeNode*, bool>> s;
        s.push({root, 1});
        while (!s.empty()){
            TreeNode* cur=s.top().first;
            bool flag=s.top().second;
            s.pop();
            if (!flag){
                ret.push_back(cur->val);
            } else if (cur){
                s.push({cur->right, true});
                s.push({cur, false});
                s.push({cur->left, true});
            }
        }
        return ret;
    }
    
    vector<int> inorder2(TreeNode* root) {
        vector<int> ret;
        stack<TreeNode*> s;
        TreeNode* cur = root;
        while (!s.empty() || cur) {
            if (cur) {
                s.push(cur);
                cur = cur->left;
            } else {
                cur = s.top();
                s.pop();
                ret.emplace_back(cur->val);
                cur = cur->right;
            }
        }
        return ret;
    }
    
    vector<int> postorder1(TreeNode* root) {
        vector<int> ret;
        stack<pair<TreeNode*, bool>> s;
        s.push({root, 1});
        while (!s.empty()){
            TreeNode* cur=s.top().first;
            bool flag=s.top().second;
            s.pop();
            if (!flag){
                ret.push_back(cur->val);
            } else if (cur){
                s.push({cur, false});
                s.push({cur->right, true});
                s.push({cur->left, true});
            }
        }
        return ret;
    }
    
    vector<int> postorder2(TreeNode* root) {
        vector<int> ret;
        stack<TreeNode*> s;
        TreeNode* cur = root;
        while (!s.empty() || cur) {
            if (cur) {
                s.push(cur);
                ret.emplace_back(cur->val);
                cur = cur->right;
            } else {
                cur = s.top();
                s.pop();
                cur = cur->left;
            }
        }
        reverse(ret.begin(), ret.end());
        return ret;
    }
    
    vector<vector<int>> threeOrders(TreeNode* root) {
        return {move(preorder1(root)), move(inorder2(root)), move(postorder2(root))};
    }
};