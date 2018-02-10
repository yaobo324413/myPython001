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

#demo4：删除变量del
var1 = 1
var2 = 10
del (var1,var2);
print (var1, var2);




















