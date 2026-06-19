class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # XYYX k = 2
        # out: 4
        # AAABABB K = 1
        # out: 5

        # AAABA 
        # no of most common char - k 
        # len of window - most common char > K
        # 1

        # map {char : frequency}
        # XYYX
        # start end = 0
        # most_frequent
        # longest_str
        # map.add(end)
        # most_frequent = max(most_frequent, end)

        # if len of window - most common char > K
        # map[start]--
        # - start++
        # longest_str = max(long..., end - start + 1)

        max_length = 0
        max_freq = 0 # no. of most common char
        start = 0
        curr_window = {}

        # X : 2
        # Y : 2
        for end in range(len(s)):
            curr_window[s[end]] = curr_window.get(s[end], 0) + 1
            max_freq = max(max_freq, curr_window[s[end]])

            if (end - start + 1) - max_freq > k:
                curr_window[s[start]] -= 1
                start += 1

            max_length = max(max_length, end - start + 1)
        
        return max_length


