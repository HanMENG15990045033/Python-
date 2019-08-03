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

s=r'\\\a'
print(s)

for i in range(0, 127):
    print(chr(i)),

seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

for a, b, c in seq:
    print(a)
    print(b)
    print(c)
    print('a={0}, b={1}, c={2}'.format(a, b, c))


def reverse_key_value_in_dict(d):
    if type(d) == dict:
        a = list(d.keys())
        b = list(d.values())
        c = dict(zip(a,reversed(b)))
    else:
        print('请输入字典')


d = {0: 'a', 1: 'b'}
reverse_key_value_in_dict(d)
e = '123'
reverse_key_value_in_dict(e)

def reverse_key_value_in_dict(d):
    if type(d) == dict:
        a = list(d.keys())
        b = list(d.values())
        c = dict(zip(b, a))
    else:
        print('请输入字典')


d = {0: 'a', 1: 'b'}
reverse_key_value_in_dict(d)
e = '123'
reverse_key_value_in_dict(e)




words = ['apple', 'bat', 'bar', 'atom','book']
by_letter_2={}

for word in words:
    letter = word[0]
    by_letter_2.setdefault(letter, []).append(word)

print(by_letter_2)


d={}
d.setdefault(a, {}).add(1)

hash({1,2,3})

t = set("Hello")
print(t)
print(id(t))
t.add('f')
print(t)
print(id(t))

words = ['apple', 'bat', 'bar', 'atom','book']


for word in words:
    letter = word[0]
    d.setdefault(letter, str)='a'

print(by_letter_2)

a = False
print(id(a))
a = True
print(id(a))


from collections import defaultdict  # 导入

d = defaultdict(list)
## 生成空列表，默认value的类型为list

d['k']
print(d)
d['k'].append(12)
print(d)


from collections import defaultdict

d = defaultdict(dict)

d['k']
print(d)
d['k'] = ('a', 'b')
print(d)

some_dict = {'a': 1, 'b': 2, 'c': 3}
dict_iterator = iter(some_dict)
dict_iterator

a=list(dict_iterator)
b=tuple(dict_iterator)
print(a)
print(b)