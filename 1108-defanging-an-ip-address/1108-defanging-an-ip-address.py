class Solution:
    def defangIPaddr(self, address: str) -> str:
        a=address.replace(".","[.]")
        return a
        