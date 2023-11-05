class Solution {
public:
    int getWinner(vector<int>& arr, int k) {
        int n=arr.size();
        if (k>=n-1) {
            int find_max=arr[0];
            for (int i:arr) find_max=max(find_max, i);
            return find_max;
        }
        int winner=0;
        int count=0;
        int compete=1;
        while (count<k) {
            if (compete>=n) compete-=n;
            if (arr[winner]>arr[compete]) {
                count++;
                compete++;
            } else {
                winner++;
                count=1;
                compete=winner+1;
            }
        }
        return arr[winner];
    }
};