import random

n = random.randint(1,100)
a = -1
guesses = 1

while(a != n):
    a = int(input("Guess a number: "))
    
    if(a>n):
        print("----------------------------Lower Number Please .----------------------------")
        guesses += 1
    elif(a<n):
        print("----------------------------Greater Number Please .----------------------------")
        guesses += 1
        
    


if (guesses == 1):
    print(f"Incredible! You guessed the correct number {n} on your 1st attempt!")
else:
    print(f"You have guessed the correct number {n} in {guesses} attempts.")



