class Solution {
public:
    string simplifyPath(string path) {
        path += '/';
        string file;
        vector<string> s;
        for (char c: path) {
            if (c != '/') {
                file += c;
                continue;
            }
            else if (file == "");
            else if (file == ".");
            else if (file == "..") {
                if (!s.empty()) s.pop_back();
            } else s.push_back(file);
            file.clear();
        }
        string ans;
        for (string &f: s) ans += "/" + f;
        if (ans == "") return "/";
        return ans;
    }
};