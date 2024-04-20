import matplotlib.pyplot as plt 
import numpy as np
import copy
from math import ceil

class Audio_Item():
    def __init__(self,filename:str) -> None:
        fileobj = open(filename , mode="rb")
        filedata = fileobj.read()
        fileobj.close()

        #размер файла
        file_size