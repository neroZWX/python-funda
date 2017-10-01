def fac(m):  # encapuslation a object 'fac' first  
    sum=1  # 
    for n in range(m):#define a range m;
        sum*=(n+1) #account any number  factorial 
        n=n+1
    return sum
def fact(n):# encapuslation anoter object 'fact'
    s=0   
    for i in (str(n)):# because 'fac' result is String ,so we need convert to 'int'
        s+=int(i)# after convert 'int' then we can add the result one number by one number
    return s

print(fact(fac(100)))# because there are  two objects encapuslation before,we can print the result directly
#Also we can use   import math 
                # print math.factorial(100)  accout the result and convert to int account the final result.