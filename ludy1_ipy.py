# -*- coding: utf-8 -*-
"""ludY1.ipy

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V-E1Lm3gAnEmGvQQ6cO5sDwZOuRMDYFm

DAY 1 *ASSIGNMENT*

**
LISTS AND ITS METHODS**
"""

LST=["ALEKHYA",150,916018,789.0,"ASD",[1,2,3]]
print(LST)
LST.append("ANUSHA")
print(LST)
LST.count(150)
print(LST)
X=LST.copy()
print(X)
LST1=["MAN",789,098.8]
LST.extend(LST1)
print(LST)
LST.index(150)
print(LST)
LST.insert(1,"high")
print(LST)
LST.pop(3)
print(LST)
LST.remove("ASD")
print(LST)
LST.reverse()
print(LST)
LST.clear()
print(LST)

"""**DICTIONARY  AND ITS FUNCTIONS**"""

dic={"name":"alekhya","age":21,"rno":150,"clg":"anits"}
print(dic)
dic.items()
dic.get("name")
print(dic)
dic.keys()
print(dic)
dic.pop("clg")
print(dic)
dic.popitem()
print(dic)
dic.update({"year":"final"})
print(dic)
alekhya=("k1","k2")
anusha=0
d=dict.fromkeys(alekhya,anusha)
print(d)
dic.values()
dic

"""**sets and its methods**"""

st={"aloo",150,78.0,"malu",150}
print(st)
st.add(567)
print(st)
st1=st.copy()
print(st1)
st2={"aloo",150}
y=st2.issubset(st)
print(y)
y=st.isdisjoint(st2)
print(y)
st.remove("malu")
print(st)
k=st.symmetric_difference(st1)
print(k)
m=st.union(st2)
print(m)

"""**tuple and its functions**"""

tup=(1,2,3,4,5,6,7,8,9,0)
u=tup.count(7)
print(u)

v=tup.index(7)
print(v)

"""**string and its function**"""

str="my name is Alekhya pappala"
print(str)
str1=str.capitalize()
print(str1)
str1=str.casefold()
print(str1)
k=str.center(80)
print(k)
l=str.count("my")
print(l)
m=str.encode()
print(m)
n=str.endswith(" ")
print(n)