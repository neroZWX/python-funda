 
 for i in range(1,101):# define a range first ,there are three results will be display
     if i%3==0 and i%5==0:# if i%3=0 i%5=0 Simultaneous
         print("fizz buzz")#then print fizz buzz(one of result)
         elif i%3==0:
             print("fizz") # just i%3=0 then print fizz
             elif i%5==0:
                 print("buzz")# just i%5=0 then print buzz
                 else:
                     print i 