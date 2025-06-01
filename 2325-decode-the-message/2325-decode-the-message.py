class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        a = []
        abc=[]
        x=0
        k = key.replace(" ","")
        k2 = str(k)
        l = list(k)
        for i in l:
            if i not in a:
                a.append(i)
        a1 = "".join(a)
        for i in range(97,123):
            abc.append(chr(i))
        m = [None]*len(message)
        for i in range(len(message)):
            if(message[i]!=" "):
                x = message[i]
                y = a1.index(x)
                m[i] = abc[y]
            elif(message[i]==" "):
                m[i]=" "
        return "".join(m)

        