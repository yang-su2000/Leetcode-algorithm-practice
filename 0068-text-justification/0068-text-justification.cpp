class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        int n=words.size();
        int space_left=maxWidth;
        vector<string> oneline;
        string one;
        vector<string> ans;
        int i=0;
        while (i<n) {
            string cur=words[i];
            if (space_left<oneline.size()+cur.size()) {
                int r=0;
                if (oneline.size()==1) {
                    while (space_left) {
                        oneline[0]+=' ';
                        space_left--;
                    }
                } else {
                    while (space_left) {
                        oneline[r]+=' ';
                        r++, space_left--;
                        if (r==oneline.size()-1) r=0;
                    }
                }
                for (string &s:oneline) one+=s;
                ans.push_back(one);
                one="";
                space_left=maxWidth;
                oneline.clear();
            } else {
                space_left-=cur.size();
                oneline.push_back(cur);
                i++;
            }
        }
        for (i=0; i<oneline.size()-1; i++) oneline[i]+=' ';
        space_left-=oneline.size()-1;
        for (string &s:oneline) one+=s;
        while (space_left) {one+=' '; space_left--;}
        ans.push_back(one);
        return ans;
    }
};