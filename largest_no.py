a = [87,54,12,65,2,5]
a.sort()
print(a[-1])

def myMax(list1):
    max  = list1[0] 
    
    for x in list1:
        if x > max:
            max = x
    
    return max

list1 = [10,50,30,40,20]

print(myMax(list1))