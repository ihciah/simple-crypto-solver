# -*- coding: utf-8 -*-

import sys
from string import maketrans,printable


class solver:
    def __init__(self):
        assert len(sys.argv)>=2
        self.c=str(sys.argv[1])
        self.level=2
        if len(sys.argv)==3:
            self.level=sys.argv[2]
        self.result=[]
        self.output()
    def rot13(self):
        return self.c.decode('rot13')
    def rot(self,n):
        from string import ascii_lowercase as lc, ascii_uppercase as uc
        lookup = maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
        return self.c.translate(lookup)
    def base64(self):
        r=''
        try:
            r=self.c.decode('base64')
        except:
            pass
        return r
    def visual_base64(self):
        c=self.c
        r=[]
        c+=((4-len(c)%4)%4)*'='
        for sub in range(0,len(c),4):
            substr=c[sub:sub+4]
            tmpr=[]
            for ca in set([substr[0].upper(),substr[0].lower()]):
                for cb in set([substr[1].upper(),substr[1].lower()]):
                    for cc in set([substr[2].upper(),substr[2].lower()]):
                        for cd in set([substr[3].upper(),substr[3].lower()]):
                            s=ca+cb+cc+cd
                            try:
                                tstr=s.decode('base64')
                                if all(c in printable for c in tstr):
                                    tmpr.append(s.decode('base64'))
                            except:
                                pass
            if len(tmpr)==0:
                return []
            r.append(tmpr)
        st=['']
        for j in r:
            sy=[]
            for jj in j:
                for i in st:
                    sy.append(i+jj)
            st=sy
        return st
    def fence(self):
        r=''
        s1end=s2=len(self.c)-len(self.c)/2
        for i in range(s1end):
            r+=self.c[i]
            if s2<len(self.c):
                r+=self.c[s2]
                s2+=1
        return r
    def output(self):
        ap=lambda x:self.result.append(x)
        if self.level==1:
            if self.base64()!='':
                ap(self.base64())
                return
            ap(self.rot13())
            ap(self.fence())
        elif self.level==2:
            self.result+=self.visual_base64()
            for i in range(26):
                ap(self.rot(i))
            ap(self.fence())
        for i in self.result:
            print i



if __name__=='__main__':
    solver=solver()
