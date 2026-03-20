class Solution:
    def substring_with_concatenation_of_all_words(
        self, s: str, words: list[str]
    ) -> list[int]:
        w_len = len(words[0])

        words_w_count = {}
        for w in words:
            words_w_count[w] = words_w_count[w] + 1 if w in words_w_count else 1

        result = []

        for i in range(w_len):
            j = i
            s_w_count = {}
            matched_words = 0

            while i + w_len <= len(s):
                i_w = s[i : i + w_len]
                i += w_len

                if i_w in words_w_count:
                    s_w_count[i_w] = s_w_count[i_w] + 1 if i_w in s_w_count else 1
                    matched_words += 1

                    while s_w_count[i_w] > words_w_count[i_w]:
                        j_w = s[j : j + w_len]
                        s_w_count[j_w] -= 1
                        matched_words -= 1
                        j += w_len

                    if matched_words == len(words):
                        result.append(j)
                else:
                    j = i
                    s_w_count = {}
                    matched_words = 0

        return result
