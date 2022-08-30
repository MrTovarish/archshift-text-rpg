import time
import numpy as np
import sys
from classes import Character, Enemy
from numpy import random

#Delay Printing (borrowed from StackOverflow)

def delay_print(s):
    #delay_print one character at a time
    #https://stackoverflow.com/questions/9246076/how-to-delay_print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.04)
   

#still unsure why - but standard procedure in python (at least for OOP) is to add:
if __name__ == '__main__':
    #Start Game:
    
    print('\n---------------------ARCHSHIFT TEXT-BASED RPG-------------------------')
    delay_print('\nYou are an Elemancer, fresh from ascendance, and ready to enter the world.')
    delay_print('\nRight now, you are in the town square, central to the overall layout')
    print('\n')
    delay_print('\nTown Crier: Ahoy there!  New to town I see?  Tell me your name, young one!')
    player_name = input('\nType in your name:  ')
    
    delay_print('\nHm, '+player_name+', haven\'t heard that one before!')
    delay_print('\nWell then, which Element did you ascend with?')
    delay_print('\nWater, Earth, Fire, or Air?')
    
    #Declare Characters:
    player = Character(player_name, '', ['kickpunch','punchkick','scream','jump'], {'Damage': 15, 'Toughness': 7}, 25, 0 , 1)
    ganger = Enemy('Ganger', 'Traitorous Gang Member', ['Stab','Kick','Pistol Shot','Grenade'], {'Damage': 8, 'Toughness': 10}, 10)
    radioactiveBear = Enemy('Radioactive Bear', 'Mutated Animal', ['Bite', 'Acid Spit', 'Claw'], {'Damage': 9, 'Toughness': 8}, 15)
    fireElemancer = Character('Blazen', 'Fire Elemancer', ['Rain of Fire', 'Ignite', 'Turn to Cinders'], {'Damage': 7, 'Toughness': 8}, 20, 0 , 0)
    waterElemancer = Character('Misty', 'Water Elemancer', ['Hydro Blast', 'Ice Spear', 'Waves of Drowning'], {'Damage': 7, 'Toughness': 9}, 20, 0 , 0)
    earthElemancer = Character('Brock', 'Earth Elemancer', ['Turn to Stone', 'Summon Rock Elemental', 'Razor Vines'], {'Damage': 7, 'Toughness': 10}, 20, 0 , 0)
    airElemancer = Character('Zephyr', 'Air Elemancer', ['Lightning Coil', 'Whirlwind', 'Crushing Pressure'], {'Damage': 7, 'Toughness': 7}, 20, 0 , 0)
    
    #Choosing which of the 4 Elemancers the Player is
    player.choose_element()
        
   #################Consider building the elemancers into arrays that can be referenced via variable 
    
    print('\n--------------------------TOWN MAP--------------------------')
    print('\nYou are currently in the town square, the central tile of the map')
    print('\nO\'s represent places you can go, X is your current location!\n')
    player.display_map()
    
    print('\n===========================CONTROLS=========================')
    print('\nTo move through the map, type: Left, Right, Up, Down')
    print('\nIn battle, type the number of the ability you want to use')    
    print('\nAny additional controls needed will be revealed at the time!')
    print('\n-----------------------------------------------------------')
    print('\n^^^^^^^^^^^^^^^^^SCROLL UP FOR INSTRUCTIONS^^^^^^^^^^^^^^^^')
    
    delay_print('\nAlright then, there\'s nothing for you here in the Town Square, explore and find Adventure!')
    delay_print('\nChoose which direction you wish to explore first!')
    
    
    ############### Consider putting a giant while loop here that checks on HP of Player and All 5 enemies.  Once the while loop breaks, the game is over.
    #enemy health check:
    
    def main_game():
        while player.health > 0:
                
            #The game once the player has control:
            #first if checks if player is in starting position (Town Square), to initiate the play state
            if player.map_array == [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][X][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]:
                delay_print('\n---You have entered the Town Square---\n')
                delay_print(f'---You currently have {player.coins} coins and {player.potions} potions\n')
                time.sleep(2)
                player.win_condition()
                player.move_map()
                
                
            #this elif is if the player moved to City Gates
            elif player.map_array == [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][O][ ]'], ['[ ][ ][X][ ][ ]'], ['[ ][O][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]:
                delay_print('---You have entered the City Gates---\n')
                delay_print(f'---You currently have {player.coins} coins and {player.potions} potions\n')
                time.sleep(2)
                player.citygates_event()
                time.sleep(1)
                player.win_condition()
                player.move_map()
                
                
            #this elif is when you are at the Museum  
            elif player.map_array == [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][X][O][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]:
                delay_print('---You have entered the Museum---\n')
                delay_print(f'---You currently have {player.coins} coins and {player.potions} potions\n')
                time.sleep(2)
                player.win_condition()
                player.museum_event()
                time.sleep(1)
                player.move_map()
                
            #this elif is when you are at the Market  
            elif player.map_array == [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][X][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]:
                delay_print('---You have entered the Market---\n')
                delay_print(f'---You currently have {player.coins} coins and {player.potions} potions\n')
                time.sleep(2)
                player.win_condition()
                player.market_event()
                time.sleep(1)
                player.move_map()
                
            #this elif is when you are at the Arena  
            elif player.map_array == [['[ ][ ][ ][ ][ ]'], ['[ ][ ][X][ ][ ]'], ['[ ][O][O][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]:
                delay_print('---You have entered the Arena---\n')
                delay_print(f'---You currently have {player.coins} coins and {player.potions} potions\n')
                time.sleep(2)
                player.win_condition()
                player.arena_gauntlet()
                time.sleep(2)
                player.move_map()
                    
            #this elif is when you are at the Outskirts  
            elif player.map_array == [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][X][ ][ ]'], ['[ ][ ][ ][ ][ ]']]:
                delay_print('---You have entered the Outskirts---\n')
                delay_print(f'---You currently have {player.coins} coins and {player.potions} potions\n')
                time.sleep(2)
                player.win_condition()
                player.outskirts_event()
                time.sleep(2)
                player.move_map()
                
            #this elif is when you are in the Wilderness
            elif player.map_array == [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][X][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]:
                delay_print('---You have entered the Wilderness---\n')
                delay_print(f'---You currently have {player.coins} coins and {player.potions} potions\n')
                time.sleep(2)
                player.win_condition()
                player.wilderness_event()
                time.sleep(2)
                player.move_map()
                
            #win condition:
            elif player.health <= 0:
                delay_print('Oh no, you died!\n')
                delay_print('--------____GAME OVER____--------')
                raise Exception('Game Over')
            else:
                print('Error, you somehow made it out of bounds!')
        
    main_game()
    
  