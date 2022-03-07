# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 01:13:58 2029

@author: user
"""

string1=input("enter first string:")
string2=input("enter second string:")
s1=string1.replace(string1[0],string2[0])
s2=string2.replace(string2[0],string1[0])
print(s1+"  "+s2)