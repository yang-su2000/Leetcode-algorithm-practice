class Solution {
    map<string, set<string>> smap;
    map<pair<string, string>, double> dmap;
public:
    double dfs(double d, string start, string end, set<string>& visited) {
        //cout << start << "->" << end << ":" << d << " ";
        if (start==end) return d;
        for (string s:smap[start]) {
            if (!visited.count(s)) {
                visited.insert(s);
                pair<string, string> p={start, s};
                double ans=dfs(d*dmap[p], s, end, visited);
                if (ans!=-1.0) return ans;
                visited.erase(s);
            }
        }
        return -1.0;
    }
    
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        int n=values.size();
        for (int i=0; i<n; i++) {
            string s1=equations[i][0];
            string s2=equations[i][1];
            pair<string, string> p={s1, s2};
            dmap[p]=values[i];
            smap[s1].insert(s2);
            p={s2,s1};
            dmap[p]=1.0/values[i];
            smap[s2].insert(s1);
        }
        /*for (auto &it:dmap) {
            cout << it.first.first << "->" << it.first.second << ":" << it.second << endl;
        }
        for (auto &it:smap) {
            cout << it.first << ":";
            for (string s:it.second) cout << s << ",";
            cout << endl;
        }*/
        n=queries.size();
        vector<double> ans(n);
        for (int i=0; i<n; i++) {
            string s1=queries[i][0];
            string s2=queries[i][1];
            if (smap.find(s1)==smap.end() or smap.find(s2)==smap.end()) ans[i]=-1.0;
            else if (s1==s2) ans[i]=1.0;
            else if (smap[s1].count(s2)) {
                pair<string, string> p={s1, s2};
                ans[i]=dmap[p];
            } else {
                set<string> visited={s1};
                double d=1.0;
                ans[i]=dfs(1.0, s1, s2, visited);
            }
        }
        return ans;
    }
};