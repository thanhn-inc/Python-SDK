from alphabet import BTC_ALPHABET
from hashlib import sha256, sha3_256
import base58

class B58:
    def __init__(self):
        pass

    def encode(self, msg):
        return base58.b58encode(msg).decode()
    
    def decode(self, str_msg: str):
        return base58.b58decode(str_msg)
    
    def encode_check(self, msg: bytes, version):
        b = bytes(version)
        b += msg
        b += B58.check_sum(msg, False)

        return self.encode(b)
    
    def decode_check(self, input: str):
        decoded = self.decode(input)
        if len(decoded) < 5:
            ""
        
        version = decoded[0]
        ck_sum = decoded[-4:]
        decoded = decoded[1:len(decoded) - 4]

        ck_sum2 = B58.check_sum(decoded)
        if ck_sum.decode() == ck_sum2.decode():
            return decoded
        
        return ""

    @staticmethod
    def check_sum(data, is_new_check_sum=False):
        if is_new_check_sum:
            return sha256(sha256(data).digest()).digest()[:4]
        else:
            return sha3_256(data).digest()[:4]

    