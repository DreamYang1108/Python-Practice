# _*_ coding: utf-8 _*_
# @DateTime : 2020/10/18 20:16
# @Author   : DreamYang
# @File     : Python100.py
# @Software : PyCharm 

# Q1：计算2的3次方
print(2**3)
print(pow(2,3))
# Q2：找出序列中的最大最小值
l = [1, 2, 3]
print(max(l))
print(min(l))
# Q3：将字符列表转为字符串
s = ["Python", "cicle", "is", "ok"]
print(" ".join(s))
# Q4：快速打印出包含所有ASCII字母（大写和小写）的字符串
import string
print(string.ascii_letters)
# Q5：让字符串居中
s = "100道python练习题"
print(s.center(50))
print(s.center(50, "*"))
# Q6：在字符串中找到子串
s = "I love python"
print(s.find("I"))
print(s.find("python"))
# Q7：让字符的首字母大写，其他字母小写
s = "i love python"
print(s.title())
print(string.capwords(s))
# Q8：清空列表内容
l = [1, 2, 3]
l.clear()
print(l)
# Q9：计算指定的元素在列表中出现了多少次
l = ["i", "love", "python", "python"]
print(l.count("python"))
# Q10：在列表末尾加入其它元素
l = [1, 2, 3]
l_2 = [4, 5, 6]
l.extend(l_2)
print(l)
# Q11：extend和列表相加的区别
l = [1, 2, 3]
l_2 = [4, 5, 6]
print(l+l_2)
# Q12：查找列表中某个元素第一次出现的索引，从0开始
l = ["i", "love", "python"]
print(l.index("love"))
# Q13：将一个对象插入到列表中
l = [1, 2, 4, 5]
l.insert(2, "three")
print(l)
# Q14：删除列表中元素
l = [1, 2, 4, 5]
print(l.pop())
print(l)
print(l.pop(1))
print(l)
# Q15：删除列表中指定元素
l = [1, 2, 4, 5, 4]
l.remove(4)
print(l)
# Q16：让列表按相反顺序排列
l = [1, 2, 3, 4, 5]
l.reverse()
print(l)
# Q17：表示只包含一个元素的元组
t = (1)
print(type(t))
t = (1, )
print(type(t))
# Q18：批量替换字符串中的元素
s = "i love python"
print(s.replace("o", "ee"))
# Q19：把字符串按照空格进行拆分
s = "i love python"
print(s.split())
# Q20：去除字符串首位的空格
s = "  i love python!"
print(s.strip())
# Q21：给字典中不存在的key指定默认值
d = {"age":18, "name":"Jack"}
print(d.get("aa", "N/A"))
# Q22：快速求1到100所有整数相加之和
print(sum(range(1, 101)))
# Q23：查出模块包含哪些属性
print(dir(string))
# Q24：快速查看某个模块的帮助文档
print(range.__doc__)
print()
# Q25：快速启动浏览器打开指定网站
import webbrowser
# webbrowser.open("http://www.python.org")
# Q26：Python里占位符怎么表示
name = "Jack"
if name == "Jack":
    print("My name is ", name)
else:
    pass
# Q27：给函数编写文档
def testfunc():
    """A test function"""
    print("This is a test function!")
print(testfunc.__doc__)
# Q28：定义私有方法
class Person:
    def __name(self):
        """使用from module import *导入时不会导入私有方法"""
        print("私有方法")
# Q29：判断一个类是否是另一个类的子类
class A:
    pass
class B(A):
    pass
print(issubclass(B, A))
# Q30：从一个非空序列中随机选择一个元素
import random
print(random.choice([1, "two", "三"]))
# Q31：查出通过from xx import xx导入的可以直接调用的方法
print(random.__all__)
# Q32：花括号{}是集合还是字典
print(type({}))
# Q33：求两个集合的并集
a = {1, 2, 3}
b = {2, 3, 4}
print(a.union(b))
print(a|b)
# Q34：求两个集合的交集
print(a&b)
print(a.intersection(b))
# Q35：求两个集合中不重复的元素
print(a^b)
print(a.symmetric_difference(b))
# Q36：求两个集合的差集
print(a-b)
print(a.difference(b))
# Q37：从一个序列中随机返回n个不同值的元素
t = (2020, 10, 18, 21, 11, 56)
print(random.sample(t, 2))
# Q38：生成两个数之间的随机实数
print(random.uniform(10, 20))
# Q39：在等差数列中随机选择一个数
print(random.randrange(0, 100, 10))
# Q40：在文件里写入字符
with open(r"./python100.txt", "w") as f:
    f.write("hello world")
# Q41：读取文件内容
with open(r"./python100.txt", "r") as f:
    s = f.read()
print(s)
# Q42：把程序打包成exe文件
"""
使用setuptools里的py2exe
"""
# Q43：把程序打包成Mac系统可运行的.app文件
"""
1、安装py2app库
2、cd到目标路径
3、py2applet --make-setup xxx.py
"""
# Q44：获取路径下所有目录名称
import sys
print(sys.path)
# Q45：Python环境下怎么执行操作系统命令
"""
使用os模块里的system方法：os.system("cd /xxx/xxx && mkdir /xxx/xxx")
"""
# Q56：将当前时间转为字符串
import time
print(time.asctime())
# Q47：将秒数转为时间数组
print(time.localtime(1698723465))
# Q48：将时间元组转换为从新纪元后的秒数
print(time.mktime((2020, 10, 18, 21, 30, 34, 7, 292, 0)))
# Q49：将字符串转为时间元组
print(time.strptime("18 Oct 2020", "%d %b %Y"))
# Q50：随机打乱列表的顺序
t = list(range(20))
print(t)
random.shuffle(t)
print(t)
# Q51：用for循环实现把字符串变成Unicode码位的列表
s = "!@#$%^&*"
codes = []
for ss in s:
    codes.append(ord(ss))
print(codes)
# Q52：用列表推导式实现把字符串变成Unicode码位的列表
codes = [ord(ss) for ss in s]
print(codes)
# Q53：打印出两个列表的笛卡尔积
colors = ["black", "white"]
sizes = ["S", "M", "L"]
shirts = ["%s %s" %(c, s) for c in colors for s in sizes]
print(shirts)
import itertools
print(list(itertools.product(colors, sizes)))
# Q54：可迭代对象拆包时，怎么赋值给占位符
player_infos = [("Kobe", "24"), ("James", "23"), ("Iverson", "3")]
for player, _ in player_infos:
    print(player)
# Q55：Python3中，用什么方式接收不确定值或参数
a, b, *c = range(6)
print(a, b, c)
# Q56：用切片将对象倒序
s = "basketball"
print(s[::-1])
# Q57：查看列表的ID
l = [1, 2, 3]
print(id(l))
# Q58：可变序列用*=（就地乘法）后，会创建新的序列吗
"""
不会创建新序列，新元素追加到老元素上
"""
l = [1, 2, 3]
print(id(l))
l *= 2
print(id(l))
# Q59：不可变序列用*=（就地乘法）后，会创建新的序列吗
"""
会创建新序列
"""
t = (1, 2, 3)
print(id(t))
t *= 2
print(id(t))
# Q60：关于+=的一道谜题
"""
t = (1, 2, [30, 40])
t[2] += [50, 60]
t变成(1, 2, [30, 40, 50, 60])且抛出TypeError异常
"""
# Q61：sort()和sorted()区别
l1 = [1, 4, 2, 3]
l2 = [1, 4, 2, 3]
j = l1.sort()
k = sorted(l2)
print(l1)
print(j)
print(l2)
print(k)
# Q62：通过reverse参数对序列进行降序排列
l = [1, 4, 2, 3]
j = sorted(l, reverse=True)
print(j)
# Q63：numpy怎么把一维数组变成二维数组
import numpy as np
a = np.arange(12)
print(a.reshape((3, 4)))
# Q64：快速插入元素到列表头部
l = [1, 2, 3, 4, 5]
l[0:0] = "python"
print(l)
l = [1, 2, 3, 4, 5]
l.insert(0, "python")
print(l)
# Q65：字典的创建方法
a = dict(one=1, two=2, three=3)
b = {"one":1, "two":2, "three":3}
c = dict(zip(["one", "two", "three"], [1, 2, 3]))
d = dict([("one", 1), ("two", 2), ("three", 3)])
e = dict({"one":1, "two":2, "three":3})
print(a, b, c, d, e)
# Q66：通过一次查询给字典里不存的键赋予新值
country_codes = {"China":86, "India":91, "US":1, "Brazil":55, "Russia":7, "Japan":81}
country_codes.setdefault("china", []).append(86)
print(country_codes)
# Q67：统计字符串中元素出现的个数
import collections
cnt = collections.Counter("aasfjslagahgkje")
print(cnt)
print(cnt.most_common(3))
# Q68：列表去重
l = ["A", "B", "C", "B", "B", "A"]
print(list(set(l)))
# Q69：求m中元素在n中出现的次数
m = {"A", "B", "C"}
n = {"B", "C", "D"}
found = 0
print(len(m&n))
# Q70：新建一个Latin-1字符集合，该集合里的每个字符的Unicode名字里都有“SIGN”这个单词，用集合推导式完成
from unicodedata import name
print({chr(i) for i in range(32, 256) if "SIGN" in name(chr(i), "")})
# Q71：查询系统默认编码方式
with open(r"./python100.txt", "w") as f:
    f.write("hello world!")
    print(f.encoding)
# Q72：修改编码方式
with open(r"./python100.txt", "w", encoding="utf-8") as f:
    f.write("hello world!")
    print(f.encoding)
# Q73：用递归实现阶乘
def factorial(n):
    return 1 if n<2 else n * factorial(n-1)
print(factorial(5))
# Q74：all([])的输出结果是多少
print(all([]))
# Q75：any([])的输出结果是多少
print(any([]))
# Q76：判断对象是否可被调用
print([callable(obj) for obj in (abs, str, 2)])
# Q77：列出对象的所有属性
print(dir(random))
# Q78：得到类的实例没有而函数有的属性列表
class C:
    pass
obj = C()
def func():
    pass
print(sorted(set(dir(func)) - set(dir(obj))))
# Q79：函数中，不想支持数量不定的定位参数，但是想支持仅限关键字参数，参数怎么定义
def f(a, *, b):
    return a, b
print(f(1, b=2))
# Q80：给函数参数和返回值注解
def function(text:str, max_len:"int>0"=80) -> str:
    pass
# Q81：不使用递归，怎么高效写出阶乘表达式
from functools import reduce
from operator import mul
def fact(n):
    return reduce(mul, range(1, n+1))
print(fact(5))
# Q82：Python什么时候执行装饰器
"""
函数装饰器在导入模块时立即执行，被装饰的函数只在调用时运行。
"""
# Q83：判断下面语句执行是否会报错
"""
b = 3
def fun(a):
    print(a)
    print(b)
    b = 7
fun(2)
报错
"""
# Q84：强制把函数中局部变量变成全局变量
b = 3
def fun(a):
    global b
    print(a)
    print(b)
    b = 7
fun(2)
# Q85：闭包中，怎么对数字、字符串、元组等不可变元素更新
def make_averager():
    count=0
    total=0
    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    return averager
avg = make_averager()
print(avg(10))
# Q86：Python2怎么解决访问外部变量报错的问题
"""
https://www.python.org/dev/peps/pep-3104/
"""
# Q87：测试代码运行的时间
t0 = time.perf_counter()
t00 = time.time()
for i in range(10000):
    pass
t1 = time.perf_counter()
t11 = time.time()
print(t1 - t0)
print(t11 - t00)
# Q88：优化递归算法，减少执行时间
import functools
@functools.lru_cache()
def fibonacci(n):
    if n<2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)
print(fibonacci(6))
# Q89：比较两个对象的值（对象中保存的数据）是否相等
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
# Q90：比较两个对象的内存地址id是否相等
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)
# Q91：格式化显示对象
from datetime import datetime
now = datetime.now()
print(format(now, "%H:%M:%S"))
print("It's now {:%I:%M%p}".format(now))
# Q92：复制一个序列并去掉后n个元素
l = [1, 2, 3, 4, 5]
j = l[:-2]
print(j)
# Q93：Python中怎么定义私有属性
"""
属性前加两个前导下划线__，尾部没有或最多一个下划线_
"""
# Q94：随机打乱一个列表里元素的顺序
from random import shuffle
l = list(range(30))
shuffle(l)
print(l)
# Q95：判断某个对象或函数是一个已知的类型
print(isinstance("aa", str))
# Q96：打印出分数
from fractions import Fraction
print(Fraction(1, 3))
# Q97：列出一个目录下所有的文件名和子文件名
"""
使用os.walk生成器函数
"""
# Q98：返回1到10的阶乘列表
import itertools, operator
print(list(itertools.accumulate(range(1, 11), operator.mul)))
# Q99：快速拼接字符串和序列形成新的列表
import itertools
print(list(itertools.chain("ABC", range(5))))
# Q100：进度条显示
import time
from tqdm import tqdm
for i in tqdm(range(1000)):
    time.sleep(.01)

