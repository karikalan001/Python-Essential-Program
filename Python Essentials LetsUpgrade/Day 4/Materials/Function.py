#!/usr/bin/env python
# coding: utf-8

# In[1]:


def great(): #Function defining
    print("Hello world")


# In[4]:


for i in range(10):
    great() #function calling


# In[11]:


def add(a=0,b=1): #Default parameter
    c = a+b
    print("Result is ",c)

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
add(num1,num2)


# In[13]:


add(b=4)


# In[30]:


v = 15 #global variable
def great():
    global v
    n = 5 #local variable
    m = 7
    v = v+n+m
    print("Result",v)
    
great()


# In[31]:


great()
print("Outside: ",v)
#print("inside: ",n)


# # Recursion function

# In[33]:


def great():
    print("Hello")
    great()

great()


# In[35]:


import sys
sys.setrecursionlimit(4000)
sys.getrecursionlimit()


# # Return statement

# In[4]:


def fact(n=5):
    if n==0:
        return 1
    return n*fact(n-1)


fact(8)


# # Ananonymous function (lambda function)

# In[6]:


def add(a,b):
    return a+b

print(add(4,7))


# In[8]:


z = lambda a,b:a+b


# In[9]:


print(z(6,8))


# In[10]:


import pyttsx3


# In[11]:


# !pip install pyttsx3


# # File Handling

# In[13]:


f1 = open(file="test.txt",mode="w")
f1.writelines("Hey everyone, I am Ritesh from Mumbai")
f1.close()


# In[16]:


f2 = open(file="test.txt",mode="a")
while True:
    var = input("Enter your words: for stop=Q ")
    if var=="Q":
        break
    else:
        f2.writelines("\n"+var)
    
f2.close()


# In[23]:


f2 = open(file="test.txt",mode="r")
f2.seek(62)
print(f2.readline())
print(f2.tell())
f2.close()


# # Sending mail from python

# In[25]:


import smtplib
#!pip install smtplib


# In[30]:


#smtp session
s = smtplib.SMTP("smtp.gmail.com",587)


#security
s.starttls()

s.login("info@gmail.com","info123") #Your mail ID
for i in range(10):
    msg = input("Enter your message here")

    s.sendmail("info@gmail.com","yourfamily@gmail.com",msg)

s.quit()


# In[ ]:




