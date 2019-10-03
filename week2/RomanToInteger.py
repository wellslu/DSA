class Solution:
    def romanToInt(self, s: str) -> int:
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        x=list(s)
        a=[]
        for i in x:
            a.append(dic[i])
        b=0
        for i in range(len(a)-1):
            if a[i]<a[i+1]:
                b=b+a[i]
        return sum(a)-2*b
