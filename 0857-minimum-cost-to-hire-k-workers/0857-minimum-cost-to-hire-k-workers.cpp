class Solution {
public:
    double mincostToHireWorkers(vector<int>& quality, vector<int>& wage, int K) {
        multimap<double, int> ratios; // min wage per quality, index
        for (int i=0; i<quality.size(); i++) {
            ratios.insert({(double)wage[i]/quality[i],i});
        }
        //cout << "ratios: ";
        //for (auto &it:ratios) cout << it.first << ":" << it.second << ", ";
        //cout << endl;
        multiset<int> qual; // min quality set to operate with size of K
        int min_qs=0; // min qualities
        auto it=ratios.begin();
        int i=0;
        while (i<K) {
            int q=quality[it->second];
            qual.insert(q);
            min_qs+=q;
            it++;
            i++;
        }
        it--;
        double ans=min_qs*(it->first);
        //cout << "ans: " << min_qs << "*" << it->first << "=" << ans << ", ";
        it++;
        while (it!=ratios.end()) {
            int q=quality[it->second];
            auto tmp=qual.end();
            tmp--;
            if (q<*tmp) {
                min_qs-=*tmp-q;
                qual.erase(tmp);
                qual.insert(q);
                ans=min(ans, min_qs*(it->first));
                //cout << min_qs << "*" << it->first << "=" << ans << ", ";
            }
            it++;
        }
        //cout << "qual: ";
        //for (int q:qual) cout << q << ", ";
        //cout << endl;
        return ans;
    }
};