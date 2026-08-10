class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for s in strs:
            encode += str(len(s)) + "#" + s

        return encode
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s) - 1:
            j = i
            substr = ""
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res