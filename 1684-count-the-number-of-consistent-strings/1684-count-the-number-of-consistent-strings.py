class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c = 0
        unique_words = []
        for w in words:
            new_w = ''.join(set(w))
            unique_words.append(new_w)
        for word in unique_words:
            if all(char in allowed for char in word):
                c += 1
        return c