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
