def pad(data, size):
    if len(data) >= size:
        return data
    data += "0" * (size - len(data)) + data

class Hash:
    """This is a representation of a hash value in Incognito Chain. Each hash value is of 32-byte long, and stored in the Big-endian fashion.
    """    
    def __init__(self, value: bytes=None):
        """Initializes a hash object.

        Args:
            
            value (bytes, optional): a 32-byte value of the hash object. Defaults to None.
        """        
        self.size = 32
        if value:
            assert len(value) == self.size
            self.value = value
    
    def __str__(self):
        return pad(self.value.hex(), 2 * self.size)
    
    def __repr__(self):
        return "{}".format(pad(self.value.hex(), 2 * self.size))
    
    def __eq__(self, h: object) -> bool:
        """Checks if two hash values are equal.

        Args:

            h (object): the hash value to be compared.
        """        
        return str(self) == str(h)
    
    def bytes(self, reverse: bool=False):
        """Returns the byte-array representation of the object.

        Args:
            
            reverse (bool, optional): Flag to indicate whether to return the list in the reversed order. Defaults to False.

        Returns:
            
            list: list of byte values of the object.
        """           
        data = list(self.value)
        if reverse:
            data.reverse()
        return data
    
    def from_bytes(self, data: list, reverse=False):
        """Constructs a hash object from list of byte values.

        Args:

            data (list): list of byte values.
            reverse (bool, optional): Flag to indicate whether to the input list is in the reversed order. Defaults to False.
        """        
        if reverse:
            data.reverse()
        data = bytes(data)
        assert len(data) == self.size
        self.value = data

    def string(self):
        """Returns the hex representation of the object.

        Returns:

            str: the hex value of the object.
        """        
        return pad(self.value.hex(), 2 * self.size)
    
    def from_string(self, data: str):
        """Constructs a hash object from a hex string.

        Args:

            data (str): a hex string representation of a 32-byte array.
        """        
        self.value = bytes.fromhex(data)
        assert len(self.value) == self.size



