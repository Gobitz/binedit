from . import *
import unittest

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

if __name__=="__main__":
    unittest.main()
