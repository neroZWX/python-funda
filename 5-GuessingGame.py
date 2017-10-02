import random #
secret_number = random.randint(1, 100)# get random number from 1 to 100
total_guess=0# set total guess time
last_guess=0# set last time guess ,because satisfy the condition for 
#it counts only as one try if they input the same number multiple times consecutively.
while True:#use while loop to implement belows conditions 
    guess=int(input("please guess the secret number:\n"))
    if last_guess != guess:# acount  total guess times
        last_guess =guess
        total_guess +=1
    if guess<secret_number:# whether guess greather secret or no
        print("you guessed number too small,try again")
    elif guess>secret_number:# use else if judge the guess number 
        print("you guessed number too large,try again") 
    else:# then finish judge
        print("Congulations you are right,\nTotal gueessed "+str(total_guess)+" times")
        break   #use "break" finish  loop. 
