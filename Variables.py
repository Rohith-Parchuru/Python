# -*- coding: utf-8 -*-
"""
Created on Sun May 31 19:52:20 2026

@author: parch
"""

x = 10
print(x)

x = [10,20,40,70,10]
x.insert(0, -25)
x.pop(3)
x.append(100)
x.sort()
x.count(10)
x.clear()
print(x)

y = ("Rohith","Ravi","Anudeep","Sasi","Ravi")

print(y)

z = {20,10,40,40,60,30}
z.pop()
z.discard(40)
z.add(30)
print(z)

data = {
        "name":"Rohith",
        "roll no":43,
        "section":'A',
        }
data.copy()
print(data)