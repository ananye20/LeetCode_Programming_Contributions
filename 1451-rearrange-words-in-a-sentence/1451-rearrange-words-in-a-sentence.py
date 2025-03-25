class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split()
        hashmap = defaultdict(list)
        
        for word in words:
            hashmap[len(word)].append(word)

        sorted_words = []
        for key in sorted(hashmap.keys()):
            sorted_words.extend(hashmap[key])
        
        s = " ".join(sorted_words)
        s = s.capitalize()
        return s
