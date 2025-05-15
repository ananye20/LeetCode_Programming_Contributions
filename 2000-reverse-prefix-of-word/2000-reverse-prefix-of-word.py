class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        i = word.index(ch)
        rev= word[:i + 1][::-1]
        remaining = word[i + 1:]
        return rev + remaining