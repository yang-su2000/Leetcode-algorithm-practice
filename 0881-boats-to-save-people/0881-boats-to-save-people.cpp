class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end());
        int l = 0, r = people.size() - 1;
        int ans = 0;
        while (l <= r) {
            if (people[r] > limit) r--;
            else if (l < r and people[l] + people[r] > limit) {
                ans++;
                r--;
            } else {
                ans++;
                l++;
                r--;
            }
        }
        return ans;
    }
};