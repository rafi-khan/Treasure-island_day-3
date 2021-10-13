print('''
*******************************************************************************
              /|                                           |\                 
             /||             ^               ^             ||\                
            / \\__          //               \\          __// \               
           /  |_  \         | \   /     \   / |         /  _|  \              
          /  /  \  \         \  \/ \---/ \/  /         /  /     \             
         /  /    |  \         \  \/\   /\/  /         /  |       \            
        /  /     \   \__       \ ( 0\ /0 ) /       __/   /        \           
       /  /       \     \___    \ \_/|\_/ /    ___/     /\         \          
      /  /         \_)      \___ \/-\|/-\/ ___/      (_/\ \      `  \         
     /  /           /\__)       \/  oVo  \/       (__/   ` \      `  \        
    /  /           /,   \__)    (_/\ _ /\_)    (__/         `      \  \       
   /  '           //       \__)  (__V_V__)  (__/                    \  \      
  /  '  '        /'           \   |{___}|   /         .              \  \     
 /  '  /        /              \/ |{___}| \/\          `              \  \    
/     /        '       .        \/{_____}\/  \          \    `         \  \   
     /                ,         /{_______}\   \          \    \         \     
                     /         /{___/_\___}\   `          \    `
*******************************************************************************
''')
print("Welcome to Treasure Island.\nYour mission is to findout the treasure\n")
cross_road = input("You are at a cross road. Where do you want to go? Type 'Left' or 'Right'\n").lower()

if cross_road == "right":
    print("Fall into a hole.\nGame Over!")
elif cross_road == "left":
    lake = input("You came to a lake. There is an island in the middle of the lake. Type 'Wait' to wait for a boat or 'Swim' or swim across?\n").lower()
    if lake == "swim":
        print("Attacked by trout.\nGame Over!")
    elif lake == "wait":
        road = input("You arrive at the island unharmed. There is a house with 3 doors One Red, one Yellow and one Blue. Which one do you choose?\n").lower()
        if road == "red":
            print("Burned by fire.\nGame Over")
        elif road == "yellow":
            print("You Win!")
        elif road == "blue":
            print("Eaten by beasts.\nGame over!")
        else:
            print("Game Over!")
    else:
        print("Attacked by trout.\nGame Over!")
else:
    print("Game Over!")


