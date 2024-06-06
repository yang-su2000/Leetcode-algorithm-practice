class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        multiset<int> m (hand.begin(), hand.end());
        while (!m.empty()) {
            int val = *m.begin();
            int curSize = 0;
            while (curSize < groupSize) {
                if (m.find(val) == m.end()) return false;
                m.erase(m.lower_bound(val));
                val++;
                curSize++;
            }
        }
        return true;
    }
};