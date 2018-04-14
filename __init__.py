from binascii import *

def israwbin(t):
    """checks whether or not t is only composed of 0 and 1""" 
    if type(t)==bytes:
        t=t.decode()
    for elt in t:
        if elt is not "1"and elt is not "0":
            return(False)
    return(True)

def hex2int(h):
    """returns int form of h\n
ex :\n
>>> hex2int("ff")\n
255"""
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
    """Object used to edit raw binary data\n
Values are stored under self.get, and can be modified with all str methods"""
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
            
    def bytefill(self):
        """Adds zeros before self.get so that len(self.get)%8==0\n
Especially useful before adding new data"""
        m=8-len(self.get)%8
        self.get=m*"0"+self.get

    def set(self,v):
        """sets self.get to v"""
        self.__init__(v)

    def add(self,v,newbyte=True):
        """adds v to self.get"""
        s=self.get
        self.__init__(v)
        if newbyte==True:
            self.bytefill()
        self.get=s+self.get
        
    def toint(self):
        """returns integer form of self.get"""
        p=len(self.get)-1
        res=0
        for elt in self.get:
            res+=int(elt)*(2**p)
            p-=1
        return(res)

    def tohex(self):
        """returns hex form of self.get"""
        r=hex(self.toint())[2:]
        while len(r)<len(self.get)/4:
            r+="0"
        return(r)

    def tobytes(self):
        """returns bytes form of self.get"""
        return(unhexlify(self.tohex()))

    def tostr(self):
        """returns string form of self.get"""
        return(self.tobytes().decode())
