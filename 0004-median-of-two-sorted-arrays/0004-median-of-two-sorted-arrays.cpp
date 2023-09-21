class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m=nums1.size(), n=nums2.size();
        if (m>n){
            swap(nums1,nums2);
            swap(m,n);
        }
        int imin=0, imax=m, mid=(m+n+1)/2, i=0, j=0;
        while (imin<=imax) {
            i=(imin+imax)/2;
            j=mid-i;
            if (i<imax && nums2[j-1]>nums1[i]){
                imin=i+1;
            } else if (i>imin && nums1[i-1]>nums2[j]){
                imax=i-1;
            } else {
                int maxl=0;
                if (i==0) maxl=nums2[j-1];
                else if (j==0) maxl=nums1[i-1];
                else maxl=max(nums1[i-1],nums2[j-1]);
                if ((m+n)%2==1) return maxl;
                
                int minr=0;
                if (i==m) minr=nums2[j];
                else if (j==n) minr=nums1[i];
                else minr=min(nums1[i],nums2[j]);
                return (maxl+minr)/2.0;
            }
        }
        return 0.0;
    }
};