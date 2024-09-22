class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        target_count = defaultdict(int)
        for char in word2:
            target_count[char] +=1
        required = len(target_count)
        current_count = defaultdict(int)
        formed = 0
        left = 0
        result = 0
        for right in range(len(word1)):
            char = word1[right]
            current_count[char] += 1
            if char in target_count and current_count[char] == target_count[char]:
                formed +=1

            while left <= right and formed == required:
                result += (len(word1) - right)

                left_char = word1[left]
                current_count[left_char] -=1

                if left_char in target_count and current_count[left_char] < target_count[left_char]:
                    formed -=1

                left +=1
        return result