# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 11:08:16 2022

@author: azizi
"""

class GrandPa:
    def __init__(self, name):
        self.grandpa_name = name
    def get_grandpa_childs(self):
        n = int(input("Enter the grandpa's childs number: "))
        mm =[]
        for i in range(n):
            mm.append(input(f"name of {i+1} child: "))
        numbers = list(range(1, n+1))
        self.grandpa_childs = dict(zip(numbers, mm))
        self.grandpa_childs.update(Father= self.grandpa_name)
        #print(dict(self.father_childs))
            
            
class Father(GrandPa):
    def __init__(self, name):
        self.father_name = name
    def get_father_childs(self):
        n = int(input("Enter the father's childs number: "))
        mm =[]
        for i in range(n):
            mm.append(input(f"name of {i+1} child: "))
        numbers = list(range(1, n+1))
        self.father_childs = dict(zip(numbers, mm))
        self.father_childs.update(Father= self.father_name)
        #print(dict(self.father_childs))
    def call_grandpa(self):
        GrandPa.__init__(self, input("Enter your grandpa's name : "))
        GrandPa.get_grandpa_childs(self)

class Child(Father):
    def __init__(self, name):
        self.child_name = name
        #self.child_childs = {"father": name }
    def get_child_childs(self):
        n = int(input("Enter the yours childs number: "))
        mm =[]
        for i in range(n):
            mm.append(input(f"name of {i+1} child: "))
        numbers = list(range(1, n+1))
        self.child_childs = dict(zip(numbers, mm))
        self.child_childs.update(Father= self.child_name)
        #print(dict(self.child_childs))
    def call_father(self):
        Father.__init__(self, input("your father's name : "))
        Father.get_father_childs(self)


son1 = Child(input("Enter your name's : "))
son1.get_child_childs()
son1.call_father()
son1.call_grandpa()
print("\nchilds of you :")
for k,v in son1.child_childs.items():
    print(f"{k} : {v}")

print("\nchilds of your father :")
for k,v in son1.father_childs.items():
    print(f"{k} : {v}")

print("\nchilds of your grandpa :")
for k,v in son1.grandpa_childs.items():
    print(f"{k} : {v}")
    