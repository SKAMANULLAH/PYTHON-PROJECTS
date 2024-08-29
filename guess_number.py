import random
n = random.randint(1,100)
a = -1
Guess = 0
while(a!= n):
 a = int(input("Guess a number :- "))
 if (a>n):
  print("Lower number please!")
  Guess = Guess +1

 elif(a<n):
  print("HIgher number please!")
  Guess = Guess +1
print(f"You have guessed the number in {Guess} attempts")
  