from __init__ import *
import unittest
from random import *

class Binedittest(unittest.TestCase):
    def test_israwbin(self):
        self.assertTrue(israwbin("0111010101"))
        self.assertTrue(israwbin(b"111011011"))
        self.assertFalse(israwbin("dfkjhgklhb"))

    def test_hex2int(self):
        self.assertEqual(hex2int("2A5Fcd"),2777037)

    def test_bytefill(self):
        b=Bin(351)
        b.bytefill()
        self.assertEqual(b.get,"0000000101011111")

    def test_set(self):
        b=Bin(36)
        b.set(255)
        self.assertEqual(b.get,"11111111")

    def test_add(self):
        pass

    def test_toint(self):
        x=randrange(1000)
        b=Bin(x)
        self.assertEqual(x,b.toint())

    def test_tohex(self):
        b=Bin(3682)
        self.assertEqual(b.tohex(),"e62")

    def test_tobytes(self):
        b=Bin("Python")
        self.assertEqual(b.tobytes(),b"Python")

    def test_tostr(self):
        b=Bin(88482574266222)
        self.assertEqual(b.tostr(),"Python")

if __name__=="__main__":
    unittest.main()
