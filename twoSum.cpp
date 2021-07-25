class Solution {
public:
    /**
     * 
     * @param numbers int整型vector 
     * @param target int整型 
     * @return int整型vector
     */
    vector<int> twoSum(vector<int>& numbers, int target) {
        map<int, int> win;
        for (int i=0; i<numbers.size(); i++){
            if (win.count(target-numbers[i])){
                return {win[target-numbers[i]], i};
            }
            win[numbers[i]]=i;
        }
        return {};
    }
};