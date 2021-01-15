import unittest
import os 

from hash import Hash

class TestHash(unittest.TestCase):
    def test_string(self):
        data = os.urandom(32)
        try:
            h = Hash(data)
            
            data2 = h.bytes()
            h2 = Hash(data)
            assert h == h2

        except Exception as e:
            print("exception thrown: {}".format(e))
            assert 1 == 0
    
    def test_bytes(self):
        data = os.urandom(32)
        data_array = list(data)
        try:
            h1 = Hash(data)
            h2 = Hash()
            h2.from_bytes(data_array)

            assert h1 == h2
            print(h1, h2)
        except Exception as e:
            print("exception thrown: {}".format(e))
            assert 1 == 0
if __name__ == '__main__':
    unittest.main()
