print(''' Welcome to 
                                                                o .,<>., o
                                                                |\/\/\/\/|
                                                                '========'
                                                                (_ SSSSSSs
                                                                )a'`SSSSSs
                                                               /_   SSSSSS
                                                               .=## SSSSS
                                                               .####  SSSSs
                                                               ###::::SSSSS
                                                              .;:::""""SSS
                                                             .:;:'  . .  \\
                                                            .::/  '     .'|
                                                           .::( .         |
                                                           :::)           \
                                                           /\(            /
                                                          /)            ( |
                                                        .'  \  .       ./ /
                                                     _-'    |\  .        |
                                   _..--..   .  /"---\      | ` |      . |
           -=====================,' _     \=(*#(7.#####()   |  `/_..   , (
                       _.-''``';'-''-) ,.  \ '  '+/// |   .'/   \  ``-.) \
                     ,'  _.-  ((    `-'  `._\    `` \_/_.'  )    /`-._  ) |
                   ,'\ ,'  _.'.`:-.    \.-'                 /   <_L   )"  |
                 _/   `._,' ,')`;  `-'`'                    |     L  /    /
                / `.   ,' ,|_/ / \                          (    <_-'     \
                \ / `./  '  / /,' \                        /|`         `. |
                )\   /`._   ,'`._.-\                       |)            \'
               /  `.'    )-'.-,' )__)                      |\            `|
              : /`. `.._(--.`':`':/ \                      ) \             \
              |::::\     ,'/::;-))  /                      ( )`.            |
              ||:::::  . .::':  :`-(                       |/    .          |
              ||::::|  . :|  |==[]=:                       .        -       \
              |||:::|  : ||  :  |  |                      /\           `     |
  ___ ___     '|;:::|  | |'   \=[]=|                     /  \                \
 |   /_  ||``|||:::::  | ;    | |  |                     \_.'\_               `-.
 :   \_``[]--[]|::::'\_;'     )-'..`._                 .-'\``:: ` .              \
  \___.>`''-.||:.__,'     SSt |_______`>              <_____:::.         . . \  _/
                                                            `+a:f:......jrei
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
user = input("You are at a cross road. Where do you want to go? Type 'left' or 'right'\n")
if user == "left" or  user == "Left":
  print("You came to lake. There is an island in the middle of the lake. Tpye 'wait' to wait for boat or Type 'swim'  to swim across.")
  input2 = input()
  if input2 == "wait" or input2 == "Wait":
    print("You arrived at the island unharmed. There is a house with three doors. one red ane blue and one yellow. Which you choose.")
    color = input()
    if color == "red" or color == "Red":
      print("Burned by fire. Game Over.")
    elif color == "blue" or color == "Blue":
      print("Eaten by beasts. Game Over")
    elif color == "yellow" or color == "Yellow":
      print("You Win.")
    else:
      print("Game Over")
  elif input2 == "swim" or input2 == "Swim":
    print("Attacked by trout. Game Over") 

  else:
    print("Game Over. You Have no choice.") 
else:
  print("You fell into hole .Game Over")

