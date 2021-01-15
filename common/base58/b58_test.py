import unittest
from b58 import B58

class TestB58(unittest.TestCase):
    def test_encode(self):
        b58 = B58()
        msg = b"hello world"
        expected = "StV1DL6CwTryKyV"
        actual = b58.encode(msg)
        assert actual == expected, "{}, {}".format(actual, expected)


        msg = b"Ahihihihihih"
        expected = "2EbCFferktU7TQSfH"
        actual = b58.encode(msg)
        assert actual == expected, "{}, {}".format(actual, expected)
    
    def test_encode(self):
        b58 = B58()
        msg = b"Ahihihihihih"
        print(list(B58.check_sum(msg, False)), list(B58.check_sum(msg, True)))
        


    
if __name__ == '__main__':
    unittest.main()