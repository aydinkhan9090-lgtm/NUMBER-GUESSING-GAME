import random
secret_number = random.randint(1,100)
print("WELCOME TO THE GUESSING GAME!")
while True:
    guess =int(input("enter your guess between 1 and 100"))
    # yaha pe user se guess input leke int use integra karega varna vo text hai 
    if guess <secret_number:
        print("too low,try again")
    elif guess >secret_number :
        print("too high,try again")
    elif guess == secret_number:
        print("congratulations! you guessed the number:", secret_number)
        break
    # yaha loop break hoga jab user sahi number guess karega 
    else:
        print("invalid input,please enter a number between 1 and 100")
            
            
            # THANK YOU FRO PLAYING THIS GAME 

    
