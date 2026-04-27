class Solution:
    def minimum_window_substring(self, s: str, t: str) -> str:
        t_char_count = {}
        for t_char in t:
            t_char_count[t_char] = t_char_count.get(t_char, 0) + 1

        s_char_count = {}
        matched = 0
        l = 0

        result = (-1, -1, float("inf"))

        for r, s_r_char in enumerate(s):
            if s_r_char in t_char_count:
                s_char_count[s_r_char] = s_char_count.get(s_r_char, 0) + 1
                if s_char_count[s_r_char] <= t_char_count[s_r_char]:
                    matched += 1

                while matched == len(t):
                    s_l_char = s[l]
                    if s_l_char in s_char_count:
                        w_length = r - l + 1
                        if result[2] > w_length:
                            result = (l, r, w_length)

                        s_char_count[s_l_char] -= 1
                        if s_char_count[s_l_char] < t_char_count[s_l_char]:
                            matched -= 1

                    l += 1

        return s[result[0] : result[1] + 1] if result[2] != float("inf") else ""
