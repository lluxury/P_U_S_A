import hashlib

def create_checksum(path):
        """
        Reads in file.  Creates checksum of file line by line.
        Returns complete checksum total for file.

        """
        fp = open(path)
        checksum = hashlib.md5()
        while True:
            buffer = fp.read(8192)
            if not buffer:break
            #checksum.update(buffer)
            checksum.update(buffer.encode())
        fp.close()
        checksum = checksum.digest()
        return checksum


# import hashlib  
  
# class Hel_String_Hash:  
#     def get(content):  
          
#         h = hashlib.new('ripemd160')  
#         h.update(content.encode())  
          
#         return h.hexdigest()  


#TypeError: Unicode-objects must be encoded before hashing


#尚未改写成功,待补完 0314