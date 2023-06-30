class Solution {
public:
    /**
     * max sum of the subarray
     * @param arr int整型vector the array
     * @return int整型
     */
    int maxsumofSubarray(vector<int>& arr) {
        int ret = 0;
        int curMaxSum = 0;
        for (int &i:arr){
            curMaxSum = max(0, curMaxSum+i);
            ret = max(ret, curMaxSum);
        }
        return ret;
    }
};