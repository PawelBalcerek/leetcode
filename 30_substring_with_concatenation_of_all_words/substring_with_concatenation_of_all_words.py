class Solution:
    def substring_with_concatenation_of_all_words(
        self, s: str, words: list[str]
    ) -> list[int]:
        w_len = len(words[0])
        w_count = len(words)

        w_counter = {}

        for word in words:
            w_counter[word] = w_counter.get(word, 0) + 1

        result = []

        for i in range(w_len):
            l = r = i
            curr_w_counter = {}
            matched_words = 0

            while r + w_len <= len(s):
                word = s[r : r + w_len]
                r += w_len

                if word in w_counter:
                    curr_w_counter[word] = curr_w_counter.get(word, 0) + 1
                    matched_words += 1

                    while curr_w_counter[word] > w_counter[word]:
                        l_word = s[l : l + w_len]
                        curr_w_counter[l_word] -= 1
                        matched_words -= 1
                        l += w_len

                    if matched_words == w_count:
                        result.append(l)
                else:
                    l = r
                    curr_w_counter = {}
                    matched_words = 0

        return result
