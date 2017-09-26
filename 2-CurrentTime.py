import time
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
 #%y year(00-99)  or %Y year(000-999)
 #%m month (01-12)
 #%d  day(0-31)
 #%H 24hour system or use ‘%I’ 12 hour system
 #%M  mins  (0-59)
 #%S  sceonds  (0-59)
 # or can  use  time.strftime('%c') Represents current time