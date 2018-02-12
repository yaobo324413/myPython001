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
# print (x)
# print (y)

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
# print (var1, var2);

#demo5：字符串
str1 = 'Hello World!';
print (str1);
print (str1[0]);
print (str1[2:7]);
print (str1[2:]);
print (str1 * 2);
print (str1 + 'test');
#判断变量类型的两种方式——type()和isinstance():
# print (type(str1));
# print (isinstance(str1,str));

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

