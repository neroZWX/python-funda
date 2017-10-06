import math   #z_next = z - ((z*z - x) / (2 * z))
def mathSqrt(x )  # X is > zero  
   s = math.sqrt
   print("math.sqrt("+str(x)+") = "+str(s))
def newtons(x,z)
    while True:
    t = z - ((z*z - x) / (2 * z))
    if(t == z or math.fabs(t-z)<0.01)
    break
     z=t 
    return t
  x =2 
  s(x)
  z=1.00
  print(newtons(x,z))
 