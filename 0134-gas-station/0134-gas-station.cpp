class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int i=0, n=gas.size();
        if (!n) return -1;
        int oil=0, bot=0, ans=0;
        while (i<n){
            oil+=gas[i]-cost[i];
            if (oil<bot) {
                bot=oil;
                ans=i+1;
            }
            i++;
        }
        return oil<0?-1:ans;
    }
};