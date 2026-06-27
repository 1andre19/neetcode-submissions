class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base = strs[0]

        for i, char in enumerate(base):
            for word in strs:
                if i  >= len(word) or char != word[i]:
                    return base[:i]
        
        return base