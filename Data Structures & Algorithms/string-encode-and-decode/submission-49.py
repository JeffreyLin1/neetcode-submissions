class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedWord = ""
        for word in strs:
            encodedWord += str(len(word)) + "#" + word
        print(encodedWord)
        return encodedWord

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            wordLength = int(s[i:j])
            i = j + 1
            j = i + wordLength
            ans.append(s[i:j])
            i = j
        return ans