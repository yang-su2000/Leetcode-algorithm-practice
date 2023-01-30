class Trie {
public:
    unordered_map<char, Trie*> children;
    string val;

    void build(string s, int i) {
        if (i == s.length()) {
            val = s;
            return;
        }
        char c = s[i];
        if (!children.count(c)) children[c] = new Trie();
        children[c]->build(s, i+1);
    }

    // bool find(string s, int i) {
    //     if (i == s.length()) return true;
    //     char c = s[i];
    //     if (children.count(c)) {
    //         return children[c]->find(s, i+1);
    //     } else return false;
    // }
};

class Solution {
    int m, n;
    vector<vector<int>> ds {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    vector<string> ans;
public:
    void backtrack(vector<vector<char>>& board, int i, int j, Trie* T) {
        if (T->val.size()) {
            ans.emplace_back(T->val);
            T->val.clear();
        }
        if (!(0 <= i && i < m && 0 <= j && j < n)) return;     
        char c = board[i][j];
        if (!T->children.count(c)) return;
        T = T->children[c];
        board[i][j] = '#';
        for (auto &d:ds) {
            int i2 = i + d[0];
            int j2 = j + d[1];
            backtrack(board, i2, j2, T);
        }
        board[i][j] = c;
    }

    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        Trie* T = new Trie();
        for (auto &word:words) T->build(word, 0);
        m = board.size();
        n = board[0].size();
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                backtrack(board, i, j, T);
            }
        }
        return ans;
    }
};