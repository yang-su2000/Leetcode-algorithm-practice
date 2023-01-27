class Trie {
public:
    unordered_map<char, Trie*> m;
    bool tail = false;

    void add(string &s, int i) {
        if (i == s.size()) {
            tail = true;
            return;
        }
        if (!m.count(s[i])) m[s[i]] = new Trie();
        m[s[i]]->add(s, i+1);
    }
    
    bool find(Trie &T, string &s, int i, int count) {
        if (i == s.size()) return tail and count >= 1;
        if (tail and T.find(T, s, i, count+1)) return true;
        if (!m.count(s[i])) return false;
        return m[s[i]]->find(T, s, i+1, count);
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