#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = 6


# In[2]:


type(a)


# In[3]:


a = "Hello"


# In[4]:


a[2]


# In[5]:


a[2]="K"


# In[6]:


b = [6,8,4,'k',5.7]


# In[8]:


b[2]="Hey"


# In[9]:


b


# In[10]:


import keyword


# In[12]:


len(keyword.kwlist)


# In[22]:


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = a+b
print("Result is ",c)


# # y = 2x+5

# In[27]:


x = int(input("Enter the number: "))
y= 2*x+5
print("Result is: ",y)


# # Operators

# In[29]:


print(3**2)


# In[37]:


14%7 #modulo


# In[41]:


5//3 #floor division 


# In[43]:


17/3


# In[44]:


4>7


# In[45]:


4<19


# In[46]:


a = 6
b = 3
a+=b # a= a+b


# In[47]:


b


# In[48]:


a


# In[50]:


3<5 and 5<12


# In[51]:


a = 6
b = 6


# In[55]:


a==b


# In[53]:


a is b


# In[54]:


a!=b


# In[56]:


a is not b


# In[57]:


l = [7,5,5,67,8,9]
7 in l


# In[58]:


67 not in l


# In[59]:


44 in l


# In[65]:


if 3<4:
    print("Hello")
elif 4>3:
    print("Hii")
else:
    print("Bye")
    


# # finding the largest number

# In[87]:


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a>b:
    if a>c:
        print("Largest number is ",a)
    else:
        print("Largest number is ",c)
if b>a:
    if b>c:
        print("Largest number is",b)
    else:
        print("Largest number is",c)

    


# # while loop

# In[89]:


a = int(input("Enter the number: "))
while a<10:
    print("hello",a)
    a=a+1
else:
    print("Bye Bye.....")


# In[93]:


a = 1
while a<=100:
    print("Hello",a)
    a+=1
    while a>20 and a<=30:
        print("Hey",a)
        a=a+1
    while a>50 and a<=70:
        print("Hiii",a)
        a=a+1


# # for loop

# In[2]:


seq = range(1,11,1)
for i in seq:
    print("Number: ",i)


# In[3]:


seq = range(10,0,-1)
for i in seq:
    print("Number: ",i)


# In[5]:


seq = ["Ritesh","Mukesh","Rahul","Priya","Shraddha"]
for i in seq:
    print("Number: ",i)


# # Nested for loop

# In[17]:


n = int(input("Enter the number: "))
for row in range(n):
    for col in range(row+1):
        print("*",end=" ")
    print()


# In[25]:


a = 1
while a<=20:
    print("Hii bro!",a)
    a+=1
    if a%5==0:
        print("Hey",a)
        continue
    


# In[35]:


a = 1
while True:
    print("Hii bro!",a)
    a=a+1
    if a==10:
        break
    
    


# In[33]:


def fun():
    pass
    
    
    
print("Hiii")


# In[36]:


for i in range(1,10):
    print(i)


# In[38]:


seq = "Ritesh"
for i in seq:
    print(i)
    


# In[41]:


seq[2]


# In[43]:


seq = ["Ritesh","Priya","Mukesh","Rahul"]
for i in seq:
    print(i)


# In[44]:


seq[0]


# In[45]:


type(seq)


# In[48]:


a = "Hey, it's Ritesh"
a


# In[50]:


z = '''seq = ["Ritesh","Priya","Mukesh","Rahul"]
for i in seq:
    print(i)'''


# In[51]:


print(z)


# In[52]:


type(z)


# # String

# In[53]:


s1 = "India"
s2 = "Mumbai"


# In[64]:


s2[0:3]


# In[54]:


s1+s2


# In[55]:


s1*3


# In[56]:


s1[0]


# In[59]:


s1[-1]


# In[60]:


s1[0]


# In[61]:


s1[-5]


# In[66]:


s1.upper()


# In[67]:


s2.lower()


# In[68]:


s3 = "hello"


# In[69]:


s3.capitalize()


# In[72]:


s3.count("l")


# In[73]:


s4 = "Hello everyone"


# In[77]:


s4.index("e",9)


# In[78]:


len(s4)


# In[79]:


len(s2)


# In[80]:


len(s3)


# In[81]:


min(s4)


# In[82]:


max(s4)


# In[83]:


n = 15
str(n)


# In[88]:


s4[3]="HP"


# # List

# In[84]:


l1 = [5,7,8,5,4.3,'hii',"ok"]

l1[-1]="Hey"


# In[85]:


l1


# In[89]:


l1[2:5]


# In[90]:


for i in l1:
    print(i)


# In[91]:


l1.append(1000)


# In[96]:


l1.insert(4,5000)


# In[97]:


l1


# In[98]:


l1.remove("hii")


# In[99]:


l1


# In[100]:


l1.pop()


# In[101]:


l1


# In[102]:


l2 = l1.copy()


# In[103]:


l1


# In[104]:


l2


# In[105]:


l3 = [7,6,4,90]
l1.extend(l3)


# In[106]:


l3


# In[107]:


l1


# In[108]:


l1.reverse()


# In[109]:


l1


# In[111]:


l1.remove("Hey")


# In[116]:


l1.sort(reverse=True)


# In[117]:


l1


# In[120]:


l1.index(4)


# In[123]:


l1.count(7)


# In[124]:


l1


# In[125]:


l1.clear()


# In[126]:


l1


# In[127]:


type(l1)


# In[128]:


l5 = [5000, 1000, 90, 8, 7, 7, 6, 5, 5, 4.3, 4]
len(l5)


# In[129]:


min(l5)


# In[130]:


max(l5)


# In[131]:


sum(l5)


# # Tuple

# In[132]:


a = (5,7,3,56,7,8.5,"Hiii")


# In[136]:


a[0:3]


# In[137]:


a = list(a)


# In[139]:


a[-1]="Hello"


# In[140]:


a


# In[141]:


a = tuple(a)


# In[142]:


a


# In[143]:


len(a)


# In[145]:


a.index(7)


# In[146]:


a.count(7)


# # Dictionary

# In[147]:


d = {"A":4,"B":5,"C":15,"D":25}


# In[148]:


type(d)


# In[150]:


len(d)


# In[151]:


min(d)


# In[152]:


max(d)


# In[153]:


d.keys()


# In[154]:


d.values()


# In[155]:


d.items()


# In[157]:


d.pop("D")


# In[158]:


d


# In[161]:


d.popitem()


# In[162]:


d


# In[163]:


d.clear()


# In[164]:


d


# In[165]:


a = ("Name","Class","Subject","Roll No")


# In[167]:


g = {}.fromkeys(a,"N")


# In[175]:


g["Name"]=["Rahul","Priya"]
g["Class"]=["12th","BE"]
g["Subject"]=["Python","ML"]
g["Roll No"]=["1235","w4653"]


# In[176]:


g


# In[179]:


s = {6,4,6,7,6,6,6}
s


# In[180]:


l = [6,8,8,76,6,5,7,8]


# In[181]:


l


# In[182]:


set(l)


# In[ ]:




