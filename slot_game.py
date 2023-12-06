import random
import time

money = 1
COST_PER_ROLL = 0.2

symbol = {
  "1": "🍒",
  "2": "🔔",
  "3": "🍋",
  "4": "🍊",
  "5": "⭐",
  "6": "💀"
}

play = input("Would you like to roll, you have £" + str(money) + " left (y/n): ")

while money > 0.2 and play == 'y':
  
  
  money -= COST_PER_ROLL
  s_1 = random.randint(1,6)
  s_2 = random.randint(1,6) 
  s_3 = random.randint(1,6)

  print(symbol[str(s_1)], symbol[str(s_2)], symbol[str(s_3)])

  #3 skulls
  if s_1 == 6 and s_2 == 6 and s_3 == 6:
    print("You lose everything!!!")
    money == 0

  #3 bells
  if s_1 == 2 and s_2 == 2 and s_3 == 2:
    print("Three bells!")
    money += 5
  
    #3 of a kind
  if s_1 == 1 and s_2 == 1 and s_3 == 1 or s_1 == 3 and s_2 == 3 and s_3 == 3 or s_1 == 4 and s_2 == 4 and s_3 == 4 or s_1 == 5 and s_2 == 5 and s_3 == 5:
    print("Three of a kind!")
    money += 1

  #2 skulls
  elif s_1 == 6 and s_2 == 6 or s_1 == 6 and s_3 == 6 or s_2 == 6 and s_3 == 6:
    print("Unlucky you lose £1")
    money -= 1.00

  #2 bells
  elif s_1 == 2 and s_2 == 2 or s_1 == 2 and s_3 == 2 or s_2 == 2 and s_3 == 2:
    print("You win £1!")
    money += 1

  #2 of the same 
  elif s_1 == s_2 or s_1 == s_2 or s_2 == s_3:
    print('You win 50p!')
    money += 0.50


  time.sleep(1)
  print("You have £" + str(round(money, 2)) + " left.")
  if money > 0.2:
    play = input("Would you like to roll, you have £" + str(round(money, 2)) + " left (y/n): ")
  else:
    play == 'n'

print("you have £" + str(round(money, 2)), "left, Thanks for playing!")