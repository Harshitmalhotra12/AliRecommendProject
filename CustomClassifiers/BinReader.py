﻿import struct
import array
import numpy as np

class BinReader(object):
    """description of class"""
    def __init__(self,filename):
        self._filename = filename

    def readline(self):
        userid = struct.unpack('i',self._file.read(4))[0]
        itemid = struct.unpack('i',self._file.read(4))[0]
        label = struct.unpack('i',self._file.read(4))[0]
        
        x = array.array('d')
        x.fromfile(self._file,self.XDim)

        return (x,userid,itemid,label)

    @staticmethod
    def readData(filename):
        reader = BinReader(filename)
        reader.open()
        data = [0] * reader.LineCount
        print reader.LineCount
        posiCount = 0
        for i in xrange(reader.LineCount):
            userid = struct.unpack('i',reader._file.read(4))[0]
            itemid = struct.unpack('i',reader._file.read(4))[0]
            label = struct.unpack('i',reader._file.read(4))[0]
            posiCount+=label
            x = array.array('d')
            x.fromfile(reader._file,reader.XDim)
            x[0] = 1
            data[i] = [userid,itemid,label] + list(x)
        reader.close()
        return (data,posiCount)

    def open(self):
        self._file = open(self._filename,'rb')
        self.LineCount = struct.unpack('i',self._file.read(4))[0]
        self.Dim = struct.unpack('i',self._file.read(4))[0]
        self.XDim = self.Dim - 3

    def close(self):
        self._file.close()

if __name__ == '__main__':
    reader = BinReader(ur'F:\AliRecommendHomeworkData\434维特征搜索作业数据\testset_20141218_3_8.bin')
    reader.open()
    for i in range(reader.LineCount):
        print np.array(reader.readline()[0])
        if raw_input() == 'e':
            break

