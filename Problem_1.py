# ## Write a program that prints your name to the console.
# name=input("Enter your name: ")
# print(name)
from openpyxl.pivot.fields import Tuple

##string----------------------------------------------------------------------------------------------
def vol(s):
    vowels="aeiouAEIOU"
    count=0
    for i in s:
        if i in vowels:
            count+=1
    return count
a="sandhya"
b=vol(a)
print(b)

def palindrome(s):
     return s==s[::-1]
a="madam"
if palindrome(a):
    print("palin")
else:
    print("not palin")

def contains_substing(string, substring):
    return substring in string
a="hello world"
b="world"
if contains_substing(a,b):
    print("substing")
else:
    print("not found substing")

def abc(s):
    words=s.split()
    return len(words)
a="hi hello how are you"
b=abc(a)
print(b)

def replace_word(s,old_w,new_w):
    return s.replace(old_w,new_w)
a="python prog"
b=replace_word(a,"prog","world")
print(b)


def dup(s):
    result=""
    for i in s:
        if i not in result:
            result+=i
    return result
a="aabbccdd"
b=dup(a)
print(b)

def non_rep(s):
    for i in s:
        if s.count(i)==1:
            return i
    return None
a="swiss"
b=non_rep(a)
print(b)

def rev(s):
    word=s.split()
    return ' '.join(reversed(word))
a="joy how are u"
b=rev(a)
print(b)

def white_space(s):
    return s.isspace()
a=" "
if white_space(a):
    print("space")
else:
    print("not space")

##tuple---------------------------------------------------------------------------------------------------
a,b=5,10
a,b=b,a
print(a)
print(b)





