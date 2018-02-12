#!/usr/bin/env python    #这句会去 环境设置env 中寻找python路径
# -*- coding:utf-8 -*-

#demo1
#定义初始值
start=1;
while True:
#判断start的值若其为51，则说明上一次已经输出了100，跳出循环
   if start==51:
     break
   print (start*2);
   start +=1;

#demo2
import sys; x= 'runoob'; sys.stdout.write(x + '\n');

#demo3
x="a"
y="b"
# 换行输出
print (x)
print (y)

print ('---------'),
# 不换行输出
print (x,'', end=''),
print (y)

# 不换行输出
print (x,y)

# #demo4：删除变量del
# var1 = 1
# var2 = 10
# del (var1,var2);
# print (var1, var2);

# #demo5：字符串
# str1 = 'Hello World!';
# print (str1);
# print (str1[0]);
# print (str1[2:7]);
# print (str1[2:]);
# print (str1 * 2);
# print (str1 + 'test');
# #判断变量类型的两种方式——type()和isinstance():
# print (type(str1));
# print (isinstance(str1,str));

# #demo6
# dict = {};
# dict['one'] = "This is one";
# dict[2] = "This is two";
# tinydict = {'name':'John','code':6734,'dept':'sales'};
#
# print (dict['one']);          # 输出键为'one' 的值
# print (dict[2]);              # 输出键为 2 的值
# print (tinydict);             # 输出完整的字典
# print (tinydict.keys());      # 输出所有键
# print (tinydict.values());    # 输出所有值

# #demo7：身份运算符
# a=2;b=2;
# print (a is b);  #True
# print (a == b);  #True
#
# c=444;d=444;
# print (c is d);  #True
# print (c == d);  #True

# #demo8:if……elif……else语句
# flag = False;
# name = 'hello';
# if name == 'python':
#     flag = True;
#     print ('welcome boss');
# elif name == 'hello':
#     print('Hello world');
# else:
#     print (name);

# #demo9
# i = 1;
# while i < 10:
#     i += 1;
#     if i%2 == 0:
#         continue;  #余数为0时，结束本次循环（即本次循环continue之后的语句不再执行），开始下一次循环
#     print (i);

# #demo10：摇筛子游戏
# import random;
# import sys;
# import time;
#
# result = [];
# while True:
#     result.append(int(random.uniform(1,7)));
#     result.append(int(random.uniform(1, 7)));
#     result.append(int(random.uniform(1, 7)));
#     print (result);
#     count = 0;
#     index = 2;
#     pointStr = "";
#     while index >= 0:
#         currPoint = result[index];
#         count += currPoint;
#         index -= 1;
#         pointStr += "";
#         pointStr += str(currPoint);
#     if count <= 11:
#         sys.stdout.write(pointStr + "->" + "小" + "\n");
#         time.sleep(1)  #睡眠1秒
#     else:
#         sys.stdout.write(pointStr + "->" + "大" + "\n");
#         time.sleep(1)  # 睡眠1秒
#     result = [];

# #demo11：十进制转二进制
# import pandas as pd;
# denum = input("输入十进制数：");
# # denum = pd.to_numeric(denum);
# denum = int(denum,10);
# # denum = 255;
# print (denum,"(10)");
# binum =[];
# #二进制数
# while denum > 0:
#     binum.append(str(denum % 2)); #栈压入
#     denum //= 2;
# print('='),
# while len(binum) > 0:
#     import sys;
#     sys.stdout.write(binum.pop());  #无空格输出print'(2)'

# #demo12：九九乘法表
# i = 1;
# while i:
#     j = 1;
#     while j:
#         print (j,"*",i,"=",i*j,''),
#         if i==j:
#             break;
#
#         j +=1;
#         if j >= 10:
#             break;
#     print("\n");
#     i += 1;
#     if i >= 10:
#         break;

# #demo13：输出 2 到 100 简的质数
# prime = [];
# for num in range(2,100):  # 迭代 2 到 100 之间的数字
#    for i in range(2,num): # 根据因子迭代
#       if num%i == 0:      # 确定第一个因子
#          break;           # 跳出当前循环
#    else:                  # 循环的 else 部分
#       prime.append(num)
# print (prime);

# #demo14：打印空心等边三角形
# rows = int(input('输入行数：'));
# for i in range(0, rows):
#     for k in range(0, 2 * rows - 1):
#         if (i != rows - 1) and (k == rows - i - 1 or k == rows + i - 1):
#             print ("-*-",end=''),
#         elif i == rows - 1:
#             if k % 2 == 0:
#                 print ("-*-",end=''),
#             else:
#                 print ("---",end=''),
#         else:
#             print ("---",end=''),
#     print ("\n");

# #demo15：打印菱形、三角形、矩形
# rows = int(input('输入列数： '));
# i = j = k = 1;  # 声明变量，i用于控制外层循环（图形行数），j用于控制空格的个数，k用于控制*的个数
# # 等腰直角三角形
# print ("等腰直角三角形");
# for i in range(0, rows):   #range(i,j)表示从i到j（不包含j）
#     for k in range(0, rows - i):
#         print ("-*-",end=''),  # 注意这里的","，一定不能省略，可以起到不换行的作用(对python 3.0以上的版本不适用)
#         k += 1;
#     i += 1;
#     print ("\n");

# # 打印实心等边三角形
# print ("打印空心等边三角形，这里去掉if-else条件判断就是实心的");
# for i in range(0, rows):  # 变量i控制行数
#     for j in range(0, rows - i):  # (1,rows-i)
#         print ("-",end=''),
#         j += 1;
#     for k in range(0, 2 * i - 1):  # (1,2*i)
#         if k == 0 or k == 2 * i - 2 or i == rows:
#             if i == rows:
#                 if k % 2 == 0:  # 因为第一个数是从0开始的，所以要是偶数打印*，奇数打印空格
#                     print ("*",end=''),
#                 else:
#                     print ("-",end=''),  # 注意这里的","，一定不能省略，可以起到不换行的作用
#             else:
#                 print ("*",end=''),
#         else:
#             print ("-",end=''),
#         k += 1;
#     print ("\n");
#     i += 1;

# # 打印菱形：|x - w/2| + |y - w/2| = w/2
# print ("打印空心等菱形，这里去掉if-else条件判断就是实心的");
# for i in range(rows):  # 变量i控制行数
#     for j in range(rows - i):  # (1,rows-i)
#         print ("-",end=''),
#         j += 1;
#     for k in range(2 * i - 1):  # (1,2*i)
#         if k == 0 or k == 2 * i - 2:
#             print ("*",end=''),
#         else:
#             print ("-",end=''),
#         k += 1;
#     print ("\n");
#     i += 1;
#     # 菱形的下半部分
# for i in range(rows):
#     for j in range(i):  # (1,rows-i)
#         print ("-",end=''),
#         j += 1;
#     for k in range(2 * (rows - i) - 1):  # (1,2*i)
#         if k == 0 or k == 2 * (rows - i) - 2:
#             print ("*",end=''),
#         else:
#             print ("-",end=''),
#         k += 1;
#     print ("\n");
#     i += 1;
# # 实心正方形
# print ("实心正方形");
# for i in range(0, rows):
#     for k in range(0, rows):
#         print ("-*-",end=''),  # 注意这里的","，一定不能省略，可以起到不换行的作用
#         k += 1;
#     i += 1;
#     print ("\n");
#
# # 空心正方形
# print ("空心正方形")
# for i in range(0, rows):
#     for k in range(0, rows):
#         if i != 0 and i != rows - 1:
#             if k == 0 or k == rows - 1:
#                 # 由于视觉效果看起来更像正方形，所以这里*两侧加了空格，增大距离
#                 print ("-*-",end=''),  # 注意这里的","，一定不能省略，可以起到不换行的作用
#             else:
#                 print ("---",end=''),  # 该处有三个空格
#         else:
#             print ("-*-",end=''),  # 这里*两侧加了空格
#         k += 1;
#     i += 1;
#     print ("\n");

#demo16：数组
# array = [1,2,5,3,6,8,4];
# print (array[0:]);
# print (array[::2]);
# print (array[2:]);
# print (array[::3]);
# print (array[::4]);
# print (array[::-1]);
# print (array[::-2]);

# #demo17：冒泡排序
# array = [1,2,5,3,6,8,4];
# for i in range(len(array) - 1, 0, -1):
#     print (i)
#     for j in range(0, i):
#         print (j,end='')
#         if array[j] > array[j + 1]:
#             #实现两个变量的互换
#             array[j], array[j + 1] = array[j + 1], array[j]
#     print ('\n')
# print (array)

#demo18：嵌套循环输出2~100之间的素数：
# i = 2;
# while (i < 100):
#     j = 2;
#     while (j <= (i / j)):
#         #若能整除则进行下面的代码
#         if not(i % j): #在python中false == 0或空，true ==1或非空。i%j取余数，当余数是0(能整除)是false，加上not变成true。不能整除相反。
#             break;
#         j = j + 1;
#     if (j > i / j):
#         print (i);
#     i = i + 1;

#demo19：创建二维列表，将需要的参数写入 cols 和 rows
# list_2d = [ [1 for i in range(5)] for i in range(4)];
# list_2d[0].append(3)
# list_2d[0].append(5)
# list_2d[2].append(7)
# print (list_2d)

#demo20:
# list01 = ['runoob', 786, 2.23, 'john', 70.2]
# list02 = [123, 'john']
# #列表截取
# print (list01[0])
# print (list01[-1])
# print (list01[0:3])

# # 列表重复
# print (list01 * 2)
#
# # 列表组合
# print (list01 + list02)
#
# # 获取列表长度
# print (len(list01))
#
# # 删除列表元素
# del list02[0]
# print (list02)
#
# # 元素是否存在于列表中
# print ('john' in list02)  # True

# # 迭代：输出数组中的每个元素
# for i in list01:
#     print (i)

# #比较两个列表的元素：
# print (cmp(list01, list02))   #python 3.0以上不存在cmp()函数
# import operator;
# print (operator.lt(2, 3));   #lt(a,b),a<b时，输出True

# # 列表最大/最小值
# print (max([0, 1, 2, 3, 4]))
# print (min([0, 1]))

# # 将元组转换为列表
# aTuple = (1,2,3,4)
# print (aTuple)
# list03 = list(aTuple)
# print (list03)

# # 在列表末尾添加新的元素
# list03.append(5)
# print (list03)

# # 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# list03.extend(list01)
# print (list03)

# # 统计某个元素在列表中出现的次数
# print (list03.count(1))

# # 从列表中找出某个值第一个匹配项的索引位置
# print (list03.index('john'))

# # 将对象插入列表
# list03.insert(0, 'hello')
# print (list03)

# # 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# print (list03.pop(0))
# print (list03)

# # 移除列表中某个值的第一个匹配项
# list03.remove(1)
# print (list03)

# # 反向列表中元素
# list03.reverse()
# print (list03)

# #对原列表进行排序
# list03.sort()
# print (list03)

#demo21:自定义函数
# def printinfo(arg1, *vartuple):
#     "打印任何输入的参数"
#     print ("输出：")
#     print (arg1)
#     for var in vartuple:
#         print (var)
#     return;
# printinfo( 10 );
# printinfo( 70, 60, 50 );

#demo22:使用 lambda 来创建匿名函数。
# sum = lambda arg1, arg2, arg3: arg1 + arg2 + arg3;
# print("相加的值为：", sum(10, 20, 30));

#demo23:return语句
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print ("函数内 : ", total)
    return total;
# 调用sum函数
print("相加的值为：", end="")
total = sum(10, 20);

#demo24:全局变量和局部变量
# total = 0;  # 这是一个全局变量
# def sum(arg1, arg2):
#     # 返回2个参数的和."
#     total = arg1 + arg2;  # total在这里是局部变量.
#     print ("函数内是局部变量 : ", total)
#     return total;
#
# # 调用sum函数
# sum(10, 20);
# print ("函数外是全局变量 : ", total)

#demo25:全局变量想作用于函数内，需加 global
# globvar = 2
# def print_globvar():
#     print(globvar)     # 没有使用 global
#
# def set_globvar_to_one():
#     global globvar     # 使用 global 声明全局变量
#     globvar = 1
#
# def print_globvar():
#     print(globvar)     # 没有使用 global
#
# print_globvar()        # 输出 1，函数内的 globvar 已经是全局变量
# set_globvar_to_one()
# print (globvar)        # 输出 1
# print_globvar()        # 输出 1，函数内的 globvar 已经是全局变量

#demop26:列表反转函数
def reverse(li):
    for i in range(0,int(len(li)/2)):
        temp = li[i];
        li[i] = li[-i-1];
        li[-i-1] = temp;
        print(i)

li = [1,2,3,4,5,6]
# print(len(li))
# print(isinstance(li[3],int))
# print(isinstance(li,str))
reverse(li)
print(li)
#直接调用reverse()函数反转
li.reverse()
print (li)




















