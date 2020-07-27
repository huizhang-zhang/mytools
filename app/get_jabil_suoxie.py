"""
Version: Python3.5
Author: OniOn
Site: http://www.cnblogs.com/TM0831/
Time: 2018/12/27 14:49

正则表达式实例
"""

from bs4 import BeautifulSoup
class getjabilsuoxie:

    def __init__(self):
        self.path = "D:/fille/str.txt"
        self.path_write = "D:/fille/str1.txt"

    def get_content(self):
        #  读取文本文件，进行读写操作
        with open(self.path, "rb") as f:
            str_con = f.read()
        print(str_con)

        # 解析表格
        # soup = BeautifulSoup(str_con,"html.parser" ) 不知道为啥会自动切除一部分
        soup = BeautifulSoup(str_con) #获取网页源代码
        tr = soup.find('table').findAll('tr')#.find定位到所需数据位置  .find_all查找所有的tr（表格）
        print(tr)
        print(len(tr))
        # 去除标签栏
        for j in tr[1:]:        #tr2[1:]遍历第1列到最后一列，表头为第0列
            td = j.find_all('td')#td表格
            key = td[0].get_text().strip()           #遍历key
            vaule = td[1].get_text().strip()  #遍历值

            # 写入文件中
            file_write = open(self.path_write, 'a', encoding = 'utf-8')
            file_write.write(key)
            file_write.write("     :")
            file_write.write(vaule)
            file_write.write('\n')


if __name__ == '__main__':
    so = getjabilsuoxie()
    so.get_content()
