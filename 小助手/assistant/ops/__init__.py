
import logging

class TextFilter():
    def filter(self,record):
        if "----" in record.msg:
            return False
        else:
            return True
        pass