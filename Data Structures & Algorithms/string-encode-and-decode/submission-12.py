class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "!" + s
        return res


    def decode(self, s: str) -> List[str]:
        strs = []

        i = 0
        while i < len(s):
            word_len, word_len_digits = 0, ""
            while s[i] != "!":
                word_len_digits += s[i]
                i += 1
            word_len = int(word_len_digits)

            strs.append(s[i + 1 : (i + 1) + word_len])
            i += word_len + 1
        return strs


