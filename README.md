# My-code
#python
#my code defines the longest first possible sequence of same letters for each from two strings

#create function which makes list of characters encountered in both strings, except spaces
def mkList(a,b):
    l=[]
    for i in a:
        if i != " " and i in b:
            l.append(i)
    return l
def func(a,b):
    res1=[]
    res2=[]
    l1=mkList(a,b)
    l2=mkList(b,a)
    #write results for first string to the list:
    c=0
    while c<len(l1):
        if l1[c] in l2:
            res1.append(l1[c])
            for i in range(0,l2.index(l1[c])+1):
                l2.pop(0)
        c+=1
    #make l2 again:
    l2=mkList(b,a)
    #write results for second string to the other list:
    d=0
    while d < len(l2):
        if l2[d] in l1:
            res2.append(l2[d])
            for i in range(0, l1.index(l2[d]) + 1):
                l1.pop(0)
        d+=1
    #choose the longest sequence:
    if len(res1)>len(res2):
        return "Result: "+" ".join(res1)
    else:
        return "Result: " +" ".join(res2)
s1=input("Enter first string: ")
s2=input("Enter second string: ")
print(func(s1,s2))
