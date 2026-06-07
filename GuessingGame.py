import sys
import random
import time

# ANSI color for spooky green
GREEN = '\033[92m'
RESET = '\033[0m'

#Asking for name and if they want to play a game
name=input(f"Hi, What's your name?").strip().capitalize()
print(f"Do you wanna play a game, {name}?")
answer=input("Yes or No?").strip().lower()
if answer == "no":
    print("Okay, Goodbye")
    sys.exit()
elif answer == "yes":
    print("Are you sureeee?")
answer2= input("Yes or No?").strip().lower()
if answer2 == "no":
    print("Maybe another time")
    sys.exit()
elif answer2 == "yes":
    print("Let's Begin!")
else:
    print("Yes or No only, Start Over")
    sys.exit()

#Guessing game
number=random.randint(1,100)

total_attempts=5
print(f"You have {total_attempts} attempts to guess the number")

attempts_left = total_attempts

while attempts_left > 0:

  try:
    guess= int(input("Enter a number between 1 and 100: ")) 
  except ValueError:
    print("Numbers only.")
    continue

  if guess== number:
    print("You're safe...for now.")
    break
  elif guess > number:
      print("Too high!")
  elif guess < number:
    print("Too low!")

  attempts_left -= 1

  if attempts_left >0:
   print(f"You have {attempts_left} {'attempt'if attempts_left== 1 else 'attempts'} left.")

else:
  print(f'The number was {number}')
  print("Better Luck Next Time!")
  time.sleep(1.5)
  print(GREEN + r"""
       ______
    .-'      `-.
   /            \
  |              |
  |,  .-.  .-.  ,|
  | )(_o/  \o_)( |
  |/     /\     \|
  (_     ^^     _)
   \__|IIIIII|__/
    | \IIIIII/ |
    \          /
     `--------`
  💀 GAME OVER 💀
""" + RESET)
