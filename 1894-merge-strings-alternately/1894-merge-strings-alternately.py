class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        if w1=="" or w2 =="":
            return w1+w2
        i=0
        w1, w2 = list(w1),list(w2)
        out=[]
        while i <len(w1) and i<len(w2):
            out.append(w1[i])
            out.append(w2[i])
            i+=1

        if i <len(w1):
            while i <len(w1):
                out.append(w1[i])
                i+=1
        if i <len(w2):
            while i <len(w2):
                out.append(w2[i])
                i+=1
        return "".join(out)