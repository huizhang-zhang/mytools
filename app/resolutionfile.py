"""
Version: Python3.5
Author: OniOn
Site: http://www.cnblogs.com/TM0831/
Time: 2018/12/27 14:49

读取文件夹文件内容，提取需要的文本，写入新的文本文件
"""
import os


class Tool:
    def __init__(self):
        self.name = "D:/fille/"

    def eachFile(self):
        fileNameList = []
        pathDir = os.listdir(self.name)

        for allDir in pathDir:
            print(allDir)

            # 判断是否是文件
            if os.path.isfile(os.path.join("D:/fille/", allDir)):
                child = os.path.join('%s%s' % (self.name, allDir))
                print(child)
                fileNameList.append(child)
        return fileNameList

    def test(self, fillName):
        #  读取文本文件，进行读写操作
        file_object = open(fillName)
        # a --追加模式  w
        file_write = open("D:/test.txt", 'a')
        try:
            line = file_object.readline()
            while line:
                array = line.split(":")
                if len(array) > 4:
                    # print(array)
                    # print(array[0])
                    date = str(array[0] + ":" + array[1] + ":" + array[2].split(" ")[0])
                    # print(date)
                    list1 = array[5].split("=")
                    # print(list1[4])
                    # print()
                    file_write.write(date)
                    file_write.write("    ")
                    file_write.write(list1[4])
                line = file_object.readline()

        finally:
            file_object.close()
            file_write.close()


if __name__ == '__main__':
    dp = Tool()
    fileNameList = dp.eachFile()
    for fileName in fileNameList:
        print(fileName)
        # dp.test(fileName)
