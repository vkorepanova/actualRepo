#!/usr/bin/env python
# coding: utf-8

# ## Упражнение 1

# In[ ]:





# In[5]:


def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

number = int(input())
print(fibonacci(number))


# In[8]:


import sys
import argparse


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('German', nargs='?')
    parser.add_argument ('-n', nargs='?')
    
    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args (sys.argv[1:])
    if namespace.n:
        print(fibonacci(int(namespace.n)))
    elif namespace.German:
        print(fibonacci(int(namespace.German)))
    else:
        print("OOOOOOOOй")


# ## Упражнение 2

# In[70]:



def print_f(func):
    def p(a):
        prom = func(a)
        if len(prom)>10:
            print("Очень много")
        if prom == []:
            print("Нет(")
    return p

@print_f
def f(a):
    l = [] 
    for i in a:
        if int(i)%2 ==0:
            l.append(i)
    return(l)

a = input().split()

f(a)


# ## Упражнение 3

# In[103]:


def swap(func):
    def h(*args, **kwargs):
        k = args[::-1]
        prom = func(*k, **kwargs)
    return h

@swap
def div(x, y, show = False):
    res = x / y
    if show:
        print(res)
    return res        

div(2, 4, show=True)


# ## Упражнение 4

# In[6]:


import time

def log(func):
    
    def p(a, b):
        start = time.time()
        answer = func(a, b)
        end = time.time()
        k = start - end
        with open("./help.txt", "w") as file:
            file.write(f"Время вызова функции: {start} \n")
            file.write(f"Входящие аргументы: {a, b} \n")
            file.write(f"Ответ: {answer} \n")
            file.write(f"Время завершения работы функции: {end} \n")
            file.write(f"Время работы функции: {end-start} \n")
    return p
    
@log    
def sum_f(a, b):
    for i in range(10000):
        k = a**(10)
    return k

sum_f(100, 6)


# In[121]:


a = 1
b = 2

print(f"a: {a}, b: {b}, c: {a + b}")
print("a: {a}".format(a=a))


# In[ ]:




