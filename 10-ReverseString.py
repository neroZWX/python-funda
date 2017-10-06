def reverse(): #http://www.jianshu.com/p/c61279736a03 soultion 
    s=input("please enter reverse string") 
    return s[::-1]# use this method to reverse string
reverse()# this method principle : This is extended slice syntax.
# It works by doing [begin:end:step] - by leaving begin and end off and specifying
#  a step of -1, it reverses a string.

