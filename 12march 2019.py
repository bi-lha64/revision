Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=(1,2,3,4)
>>> a
(1, 2, 3, 4)
>>> b=("a","b","c","d")
>>> b
('a', 'b', 'c', 'd')
>>> a.append(5)

>>> b.remove("c")

>>> a.pop()

>>> a.reverse()

>>> for x in a:
	print(x)

	
1
2
3
4
>>> d=[x for x in a]
>>> 
>>> d
[1, 2, 3, 4]
>>> c=list(a)
>>> c
[1, 2, 3, 4]
>>> d=[x for x in a]
>>> d
[1, 2, 3, 4]
>>> a
(1, 2, 3, 4)
>>> f=a+b
>>> f
(1, 2, 3, 4, 'a', 'b', 'c', 'd')
>>> a*3
(1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)
>>> "b" in b
True
>>> "e" in b
False
>>> 5 in a
False
>>> 1 in a
True
>>> 
>>> x[1,2,3,4]

>>> y=( x for z in x)

>>> y=( z for z in x)

>>> a=[1,2,3,1,4,2,5,3,7]
>>> a
[1, 2, 3, 1, 4, 2, 5, 3, 7]
>>> b=set(a)
>>> b
{1, 2, 3, 4, 5, 7}
>>> c={"a","b","c","c"}
>>> c
{'b', 'c', 'a'}
>>> c={"a","b","a","c","c"}
>>> c
{'b', 'c', 'a'}
>>> d={"a","A","b","B","a","B"}
>>> d
{'A', 'b', 'B', 'a'}
>>> s1={1,2,3,4}
>>> s1
{1, 2, 3, 4}
>>> s2={3,4,5,6}
>>> s2
{3, 4, 5, 6}
>>> s2.add(7)
>>> s1={1,2,3,4}
>>> s2={3,4,5,6}
>>> s2.add(7)
>>> s2
{3, 4, 5, 6, 7}
>>> s2.remove(7)
>>> s2
{3, 4, 5, 6}
>>> s1.discard(4)
>>> s1
{1, 2, 3}
>>> s2.remove(7)

>>> s1.discard(4)
>>> s1
{1, 2, 3}
>>> s1.difference(s2)
{1, 2}
>>> s2.difference(s1)
{4, 5, 6}
>>> s1.intersection(s2)
{3}
>>> s2.intersction(s2)

>>> s2.intersection(s2)
{3, 4, 5, 6}
>>> s2.union(s1)
{1, 2, 3, 4, 5, 6}
>>> s1.union(s2)
{1, 2, 3, 4, 5, 6}
>>> s1.extend(s2)

>>> s1.extend(s2)...

>>> s1.update({1,2,3,4})
>>> s1
{1, 2, 3, 4}
>>> s2.update({10,11,12})
>>> s2
{3, 4, 5, 6, 10, 11, 12}
>>> codes={"kenya":254 "uganda":256 "tanzania":255}

>>> codes={"kenya":254,"uganda":256,"tanzania":255}
>>> codes
{'kenya': 254, 'uganda': 256, 'tanzania': 255}
>>> codes["kenya"]
254
>>> codes["kenya"=250
	  

>>> codes["kenya"]=250
	  
>>> codes
	  
{'kenya': 250, 'uganda': 256, 'tanzania': 255}
>>> codes["Rwanda"]=252
	  
>>> codes
	  
{'kenya': 250, 'uganda': 256, 'tanzania': 255, 'Rwanda': 252}
>>> codes.pop("Rwanda")
	  
252
>>> codes
	  
{'kenya': 250, 'uganda': 256, 'tanzania': 255}
>>> codes.keys()
	  
dict_keys(['kenya', 'uganda', 'tanzania'])
>>> codes.value()
	  

>>> codes.values()
	  
dict_values([250, 256, 255])
>>> 
	  
>>> for key in codes.keys()1:
	  
SyntaxError: invalid syntax
>>> for key in codes.keys():
	  print(key)

	  
kenya
uganda
tanzania
>>> for value in codes.values():
	  print(value)

	  
250
256
255
>>> for v in codes.values():
	  print(v)

	  
250
256
255
>>> n=dict()
	  
>>> n
	  
{}
>>> m=dict()
	  
>>> m["a"]=10
	  
>>> m["b"]=20
	  
>>> m
	  
{'a': 10, 'b': 20}
>>> m["b"]=20
	  
>>> m
	  
{'a': 10, 'b': 20}
>>> a={0,1,2,3,4,5,6,7,8,9,10}
	  
>>> a
	  
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
>>> a.keys()
	  

>>> 
	  
>>> a={0,1,2,3,4,5,6,7,8,9,10}
	  
>>> a
	  
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
>>> a=(0,10)
	  
>>> a
	  
(0, 10)
>>> a=range(0,10)
	  
>>> a
	  
range(0, 10)
>>> for a in range in z:
	  print(a)

	  

>>> a=range(0,10)
	  
>>> a
	  
range(0, 10)
>>> for a in z:
	  print(a)

	  

>>> a=range(0,10)
	  
>>> a
	  
range(0, 10)
>>> for c in z:
	  print(c)

	  

>>> a=range(0,10)
	  
>>> a
	  
range(0, 10)
>>> for c ina
	  

>>> a=range(0,10)
	  
>>> a
	  
range(0, 10)
>>> for c in a:
	  print(c)

	  
0
1
2
3
4
5
6
7
8
9
>>> d=[c*c for c in a]
	  
>>> b
	  
{1, 2, 3, 4, 5, 7}
>>> d={c*c for c in a}
	  
>>> d
	  
{0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
>>> 
	  
>>> a.keys
	  

>>> range={0,10}
	  
>>> range
	  
{0, 10}
>>> range.keys
	  

>>> range={0:1:2:3:4:5:6:7:8:9:10}
	  
SyntaxError: invalid syntax
>>> range={0,1,2,3,4,5,6,7,8,9,10}
	  
>>> range
	  
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
>>> range.keys()
	  

>>> for key in range.keys:
	  print(keys)

	  

>>> for key in range.keys:
	  print(key)

	  

>>> range={0,1,2,3,4,5,6,7,8,9,10}
	  
>>> range
	  
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
>>> for value in values:
	  print(value)

	  

>>> for key in keys:
	  print(key)

	  

>>> for range in keys:
	  print(keys)

	  

>>> for keys in dict:
	  print(keys)

	  

>>> for a in thisdict:
	  print(thisdict[a])

	  

>>> a=range(0,10)
	  

>>> s=dict()
	  
>>> s[2]=2*2
	  
>>> s
	  
{2: 4}
>>> range=(0,10)
	  
>>> range
	  
(0, 10)
>>> range=dict()
	  
>>> range[2]=2*2
	  
>>> range
	  
{2: 4}
>>> range=dict()
	  
>>> range=[0]=0*10
	  
SyntaxError: can't assign to literal
>>> range=dict()
	  
>>> range[]
	  
SyntaxError: invalid syntax
>>> range=dict()
	  
>>> r=dict
	  
>>> 
	  
>>> 
	  

9
>>> r=dict()
	  
>>> for p in range (10):
	  r[p]=p*p

	  
Traceback (most recent call last):
  File "<pyshell#188>", line 1, in <module>
    for p in range (10):
TypeError: 'dict' object is not callable
>>> r=dict()
	  
>>> for p in range(10)
	  
SyntaxError: invalid syntax
>>> for p in range(10):
	  m[p]=p*p
	  print(m)

	  

>>> m=dict()
	  
>>> m[]
	  
SyntaxError: invalid syntax
>>> m=dict()
	  
>>> for p in range
	  
SyntaxError: invalid syntax
>>> for p in range(10):
	  m[p]=p*p
	  print(m)

	  

>>> fruits{"melon","apple","mango","orange","grapes","lemon","bananas","kiwi","avacado","pineapple"}
	  
SyntaxError: invalid syntax
>>> fruits["melon","apple","mango","orange","grapes","lemon","bananas","kiwi","avacado","pineapple"]
	  

>>> fruits=["melon","apple","mango","orange","grapes","lemon","bananas","kiwi","avacado","pineapple"]
	  
>>> print(dict)
	  
<class 'dict'>
>>> f"


		
	  print
	  
SyntaxError: EOL while scanning string literal
>>> 
	  
>>> for x in fruits:
	  print("melon")

	  
melon
melon
melon
melon
melon
melon
melon
melon
melon
melon
>>> length("melon")
	  

>>> for fruit in fruits:
	  print(fruits)

	  
['melon', 'apple', 'mango', 'orange', 'grapes', 'lemon', 'bananas', 'kiwi', 'avacado', 'pineapple']
['melon', 'apple', 'mango', 'orange', 'grapes', 'lemon', 'bananas', 'kiwi', 'avacado', 'pineapple']
['melon', 'apple', 'mango', 'orange', 'grapes', 'lemon', 'bananas', 'kiwi', 'avacado', 'pineapple']
['melon', 'apple', 'mango', 'orange', 'grapes', 'lemon', 'bananas', 'kiwi', 'avacado', 'pineapple']
['melon', 'apple', 'mango', 'orange', 'grapes', 'lemon', 'bananas', 'kiwi', 'avacado', 'pineapple']
['melon', 'apple', 'mango', 'orange', 'grapes', 'lemon', 'bananas', 'kiwi', 'avacado', 'pineapple']
['melon', 'apple', 'mango', 'orange', 'grapes', 'lemon', 'bananas', 'kiwi', 'avacado', 'pineapple']
['melon', 'apple', 'mango', 'orange', 'grapes', 'lemon', 'bananas', 'kiwi', 'avacado', 'pineapple']
['melon', 'apple', 'mango', 'orange', 'grapes', 'lemon', 'bananas', 'kiwi', 'avacado', 'pineapple']
['melon', 'apple', 'mango', 'orange', 'grapes', 'lemon', 'bananas', 'kiwi', 'avacado', 'pineapple']
>>> for x in fruits:
	  print(x)

	  
melon
apple
mango
orange
grapes
lemon
bananas
kiwi
avacado
pineapple
>>> for x in dict:
	  print(x)

	  

>>> fruits=["melon","apple","mango","orange","grapes","lemon","bananas","kiwi","avacado","pineapple"]
	  
>>> g=dict()
	  
>>> for x in fruits:
	  g[x]=len(x)

	  
>>> print(g)
	  
{'melon': 5, 'apple': 5, 'mango': 5, 'orange': 6, 'grapes': 6, 'lemon': 5, 'bananas': 7, 'kiwi': 4, 'avacado': 7, 'pineapple': 9}
>>> 
