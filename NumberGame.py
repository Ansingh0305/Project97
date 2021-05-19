import random
n = random.randint(1, 9)
o = 0
print("Number Guessing Game")
print("Enter A Number Between 1-9")

while o < 5:

    m = int (input("Enter Your Guess :"))
    
    if(m==n):
        print("Correct answer you won")
        break

    elif(m<n):
        print('Nope the original number is greater than ',m)
    else:
        print("Nope the original number is smaller than ",m)
    
    o = o + 1

if not o < 5 :
    print("You Lose, The Number is ", n)
    
    
