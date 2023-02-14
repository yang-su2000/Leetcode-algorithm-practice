class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ab = reduce(xor, nums)
        # get rightmost 1 of ab, use this to separate nums to 2 buckets
        # one bucket has a and some duplicates
        # the other bucket has b and other duplicates
        bucket = ab & (-ab)
        ans0 = 0
        ans1 = 0
        for i in nums:
            if i & bucket:
                ans0 ^= i
            else:
                ans1 ^= i
        return [ans0, ans1]
        