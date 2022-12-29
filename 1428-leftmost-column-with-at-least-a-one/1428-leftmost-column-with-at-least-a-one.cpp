/**
 * // This is the BinaryMatrix's API interface.
 * // You should not implement it, or speculate about its implementation
 * class BinaryMatrix {
 *   public:
 *     int get(int row, int col);
 *     vector<int> dimensions();
 * };
 */

class Solution {
public:
    int leftMostColumnWithOne(BinaryMatrix &binaryMatrix) {
        vector<int> dim = binaryMatrix.dimensions();
        int l = 0, r = dim[1];
        for (int i=0; i<dim[0]; i++) {
            while (l < r) {
                int mid = (l + r) / 2;
                int val = binaryMatrix.get(i, mid);
                if (val) r = mid;
                else l = mid+1;
            }
            l = 0;
        }
        if (r == dim[1]) return -1;
        return r;
    }
};