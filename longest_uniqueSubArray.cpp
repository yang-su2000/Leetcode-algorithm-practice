class Solution {
public:
    /**
     * 
     * @param arr int整型vector the array
     * @return int整型
     */
    int maxLength(vector<int>& arr) {
        map<int, int> s;
        int maxCount = 0;
        for (int i = 0, j = 0; i < arr.size(); i++){
            if (s.count(arr[i])) {
                j = max(j, s[arr[i]] + 1);
            }
            s[arr[i]] = i;
            maxCount = max(maxCount, i - j + 1);
        }
        return maxCount;
    }
};