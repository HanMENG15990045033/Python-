# ## 关于zip的说明，https://blog.csdn.net/qq_37383691/article/details/75271172
# ## 补充一下zip()函数 多个列表合成一个列表，元素为对应位置元素组成的元组
#
a = [1,2,3]
b = [4,5,6]
c = [7,8,9,10]
zipped_1 = zip(a,b)
zipped_2 = zip(a,b,c)
print(list(zipped_1))

a = ['a0', 'a1', 'a2']
b = ['b0', 'b1', 'b2', 'b3']
c = ('c0', 'c1', 'c2')
d = ('d0', 'd1', 'd2')
f = '0123456'

ab = zip(a, b)
print(list(ab))
ac = zip(a, c)
print(list(ac))
af = zip(a, f)
print(list(af))


# print("\n1.解压前的zipped_1")
# print(zipped_1) ## 只会打出一个文件名一样的东西

# ## list函数以一个元组为参数转化为列表
# ## 想看内容用list，但list之后似乎无法解压了
# print("\n2.解压的zipped_1")
# print(*zipped_1) ## (1, 4) (2, 5) (3, 6)
# print("\n3.解压之后的zipped_1")
# print(zipped_1)
# print("\n4.解压之后的*zipped_1")
# print(*zipped_1)
#
#
# print("\n5.解压前的zipped_2")
# print(zipped_2)
# # print(list(zipped_2)) ## 用list之后也无法提出元素
# print("\n6.解压的zipped_2元组提取出来")
# x, y, z = [*zipped_2]
# print(x)
# print(y)
# print(z)
#
# print("\n7.解压之后的zipped_2")
# print(zipped_2)
# print(list(zipped_2))
# ## 解压之后再用list，返回一个空集
# print("\n8.解压之后没法再解压，就返回一个空")
# print(*zipped_2)
#


# 关于groupby的说明

from itertools import groupby ## 导入分组，月份、周数、周几，在计算每组的平均值

print('groupby的结果')
## 补充groupby 分组 按指定位置的元素
test = [(1, 5), (1, 4), (1, 3), (1, 2), (2, 4), (2, 3), (3, 5)]
temp = groupby(sorted(test), key=lambda x: x[0])
## 得到一个列表，{（分类元素，剩下的东西）}
## 元组零位元素，1是一组，2一组，3一组
print('1. list处理之前打印temp')
print(temp)
# print('2. list处理的temp')
# print(list(temp))
# print('3. list处理过的temp')
# print(temp)
print('4. list未处理过的temp分组打印')
for a, b in temp:
    print(list(b))

a = [1,2,3,4,10,11,12,13,20,21]
b = sorted(a)
print(b)

a = ['1','2','3','4','5','11','12','13','20','21']
b = sorted(a)
print(b)

a = ['1','2','3','4','5','11','12','13','20','21']
c = [int(x) for x in a]
print(c)
print(sorted(c))

a = ['1','2','3','4','5','11','12','13','20','21']
for x in a:
    if x == '1':
        a[a.index(x)] = '01'
    elif x == '2':
        a[a.index(x)] = '02'
    elif x == '3':
        a[a.index(x)] = '03'
    elif x == '4':
        a[a.index(x)] = '04'
    elif x == '5':
        a[a.index(x)] = '05'
    elif x == '6':
        a[a.index(x)] = '06'
    elif x == '7':
        a[a.index(x)] = '07'
    elif x == '8':
        a[a.index(x)] = '08'
    elif x == '9':
        a[a.index(x)] = '09'

print(a)
print(sorted(a))


c = [int(x) for x in a]
print(c)
print(sorted(c))


s = '\a'
print(s)

s = '\ab'
print(s)

s = 'b\a'
print(s)

s = '\'
print(s)

s = '\\'
print(s)

s = '\\\'
print(s)

s = '\\\\'
print(s)

s = '\\\a'
print(s)

s = '\24'
print(s)