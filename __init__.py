from binascii import *

def israwbin(t):
    if type(t)==bytes:
        t=t.decode()
    for elt in t:
        if elt is not "1"and elt is not "0":
            return(False)
    return(True)

def hex2int(h):
    if type(h)==bytes:
        h=h.decode()
    h=h.lower()
    c="0123456789abcdef"
    p=len(h)-1
    res=0
    for elt in h:
        res+=c.find(elt)*(16**p)
        p-=1
    return(res)

class Bin():
    def __init__(self,v):
        if type(v)==float:
            v=int(v)
        elif type(v)==bytes:
            if israwbin(v):
                self.get=v.decode()
            else:
                v=hex2int(hexlify(v))
        elif type(v)==str:
            if israwbin(v):
                self.get=v
            else:
                v=v.encode()
                v=hex2int(hexlify(v))
        if type(v)==int:
            self.get=bin(v)[2:]
            
    def octetfill(self):
        m=8-len(self.get)%8
        self.get=m*"0"+self.get

    def set(self,v):
        self.__init__(v)

    def add(self,v,newoctet=True):
        s=self.get
        self.__init__(v)
        if newoctet==True:
            self.octetfill()
        self.get=s+self.get
        
    def toint(self):
        p=len(self.get)-1
        res=0
        for elt in self.get:
            res+=int(elt)*(2**p)
            p-=1
        return(res)

    def tohex(self):
        r=hex(self.toint())[2:]
        while len(r)<len(self.get)/4:
            r+="0"
        return(r)

    def tobytes(self):
        return(unhexlify(self.tohex()))

    def tostr(self):
        return(self.tobytes().decode())
