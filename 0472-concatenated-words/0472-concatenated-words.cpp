class Trie {
    vector<Trie*> m;
    bool tail;
public:
    Trie() {
        m.resize(26, nullptr);
        tail = false;
    }
    
    void add(string &s, int i) {
        if (i == s.size()) {
            tail = true;
            return;
        }
        int c = s[i]-'a';
        if (!m[c]) m[c] = new Trie();
        m[c]->add(s, i+1);
    }
    
    bool find(Trie &T, string &s, int i, int count) {
        if (i == s.size()) return tail and count >= 1;
        if (tail and T.find(T, s, i, count+1)) return true;
        int c = s[i]-'a';
        if (!m[c]) return false;
        return m[c]->find(T, s, i+1, count);
    }
};

class Solution {
public:
    vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {
        Trie T = Trie();
        for (string &word: words) T.add(word, 0);
        vector<string> ans;
        for (string &word: words) {
            if (T.find(T, word, 0, 0)) ans.emplace_back(word);
        }
        return ans;
    }
};