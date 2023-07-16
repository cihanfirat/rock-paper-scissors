rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choose=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
if choose==0:
  print(f"You chose: \n {rock}")
elif choose==1:
  print(f"You chose: \n {paper}")
elif choose==2:
  print(f"You chose: \n {scissors}")
else:
  print("Invalid input. Game over!")

a=random.randint(0,2)
if a==0:
  print(f"Computer chose: \n {rock}")
elif a==1:
  print(f"Computer chose: \n {paper}")
else:
  print(f"Computer chose: \n {scissors}")
  
if choose==0 and a==0:
  print("It's Draw.")
elif choose==1 and a==1:
  print("It's Draw.")
elif choose==2 and a==2:
  print("It's Draw.")
  
elif choose==1 and a==0:
  print("You win.")
elif choose==1 and a==2:
  print("You lose.")
  
elif choose==0 and a==1:
  print("You lose.")
elif choose==0 and a==2:
  print("You win.")

elif choose==2 and a==0:
  print("You lose.")
elif choose==2 and a==1:
  print("You win.")