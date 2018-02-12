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

#demo13：输出 2 到 100 简的质数
prime = [];
for num in range(2,100):  # 迭代 2 到 100 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         break;           # 跳出当前循环
   else:                  # 循环的 else 部分
      prime.append(num)
print (prime);





















