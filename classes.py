import time
import numpy as np
import sys
from numpy import random

def delay_print(s):
    #print one character at a time
    #https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.04)
   

#Create Player class
class Character:
    #define init function - this sets the initial state of the Character class.  Basically
    #this is just defininig the properties we're going to generate for each Character.
    def __init__(self, name, element, abilities, stats, health, bars = '', map_array = [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][X][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']] ):
        self.name = name
        self.element = element
        self.abilities = abilities
        self.damage = stats['Damage']
        self.toughness = stats['Toughness']
        self.bars = bars
        self.health = health
        self.map_array = map_array
        
        ####BUILD MULTIDIMENSIONAL ARRAY OF MAP TO STORE LOCATION STATE
    #global map_array    
    
    
    def choose_element(self):
        global fireElemancer
        global waterElemancer
        global earthElemancer
        global airElemancer
    
        
        chosen_element = ''
        while chosen_element != ('Water' or 'Fire' or 'Earth' or 'Air'):
            chosen_element = input('\nChoose Element:  ')
            self.element = chosen_element
            if chosen_element == ('Earth'):
                delay_print('Aha! an ' + chosen_element + ' Elemancer!  Good, good, we\'ve been short on those.')
                fireElemancer = Character('Blazen', 'Fire Elemancer', ['Rain of Fire', 'Ignite', 'Turn to Cinders'], {'Damage': 5, 'Toughness': 8}, 20)
                fireElemancer.damage = fireElemancer.damage * 1.5
                waterElemancer = Character('Misty', 'Water Elemancer', ['Hydro Blast', 'Ice Spear', 'Waves of Drowning'], {'Damage': 4, 'Toughness': 9}, 20)
                airElemancer = Character('Zephyr', 'Air Elemancer', ['Lightning Coil', 'Whirlwind', 'Crushing Pressure'], {'Damage': 6, 'Toughness': 7}, 20)
                airElemancer.damage = airElemancer.damage / 2
                break
            elif chosen_element == ('Air'):
                delay_print('Aha! an ' + chosen_element + ' Elemancer!  Good, good, we\'ve been short on those.')
                fireElemancer = Character('Blazen', 'Fire Elemancer', ['Rain of Fire', 'Ignite', 'Turn to Cinders'], {'Damage': 5, 'Toughness': 8}, 20)
                waterElemancer = Character('Misty', 'Water Elemancer', ['Hydro Blast', 'Ice Spear', 'Waves of Drowning'], {'Damage': 4, 'Toughness': 9}, 20)
                waterElemancer.damage = waterElemancer.damage / 2
                earthElemancer = Character('Brock', 'Earth Elemancer', ['Turn to Stone', 'Summon Rock Elemental', 'Razor Vines'], {'Damage': 3, 'Toughness': 10}, 20)
                earthElemancer.damage = earthElemancer.damage * 1.5
                break
            elif chosen_element == ('Fire'):
                delay_print('Aha! a ' + chosen_element + ' Elemancer!  Good, good, we\'ve been short on those.')
                waterElemancer = Character('Misty', 'Water Elemancer', ['Hydro Blast', 'Ice Spear', 'Waves of Drowning'], {'Damage': 4, 'Toughness': 9}, 20)
                waterElemancer.damage = waterElemancer.damage / 2
                earthElemancer = Character('Brock', 'Earth Elemancer', ['Turn to Stone', 'Summon Rock Elemental', 'Razor Vines'], {'Damage': 3, 'Toughness': 10}, 20)
                earthElemancer.damage = earthElemancer.damage * 1.5
                airElemancer = Character('Zephyr', 'Air Elemancer', ['Lightning Coil', 'Whirlwind', 'Crushing Pressure'], {'Damage': 6, 'Toughness': 7}, 20)
                break
            elif chosen_element == ('Water'):
                delay_print('Aha! a ' + chosen_element + ' Elemancer!  Good, good, we\'ve been short on those.')
                airElemancer = Character('Zephyr', 'Air Elemancer', ['Lightning Coil', 'Whirlwind', 'Crushing Pressure'], {'Damage': 6, 'Toughness': 7}, 20)
                airElemancer.damage = airElemancer.damage * 1.5
                earthElemancer = Character('Brock', 'Earth Elemancer', ['Turn to Stone', 'Summon Rock Elemental', 'Razor Vines'], {'Damage': 3, 'Toughness': 10}, 20)
                fireElemancer = Character('Blazen', 'Fire Elemancer', ['Rain of Fire', 'Ignite', 'Turn to Cinders'], {'Damage': 5, 'Toughness': 8}, 20)
                fireElemancer.damage = fireElemancer.damage / 2
                break
            else:
                delay_print('Hmmm, that\'s not a valid Element, try again!')
                
                
    def arena_gauntlet(self):
        delay_print('Welcome to the Arena!  Here you will fight through a gauntlet of fellow Elemancers\n')
        delay_print('in a series of Trials. Should you defeat each of the Elemancers with whom you do not\n')
        delay_print('share the same Element, you will be declared victorious!\n')
        delay_print('Would you like to begin the Trial now, or come back later?\n')
        print('Hint: You will want plenty of Health Potions!\n')
        yes_or_no = input('Start Trial Now?  Yes / No: ')
        if yes_or_no == 'Yes':
            while self.health > 0:
                if self.element == ('Earth'):
                    self.fight(airElemancer)
                    time.sleep(2)
                    self.fight(waterElemancer)
                    time.sleep(2)
                    self.fight(fireElemancer)
                    delay_print('Congratulations!  You have passed your Trial and defeated the Gauntlet!')
                    break
                    
                elif self.element == ('Air'):
                    self.fight(waterElemancer)
                    time.sleep(2)
                    self.fight(fireElemancer)
                    time.sleep(2)
                    self.fight(earthElemancer)
                    delay_print('Congratulations!  You have passed your Trial and defeated the Gauntlet!')
                    break
                    
                elif self.element == ('Fire'):
                    self.fight(earthElemancer)
                    time.sleep(2)
                    self.fight(airElemancer)
                    time.sleep(2)
                    self.fight(waterElemancer)
                    delay_print('Congratulations!  You have passed your Trial and defeated the Gauntlet!')
                    break
                    
                elif self.element == ('Water'):
                    self.fight(fireElemancer)
                    time.sleep(2)
                    self.fight(earthElemancer)
                    time.sleep(2)
                    self.fight(airElemancer)
                    delay_print('Congratulations!  You have passed your Trial and defeated the Gauntlet!')
                    break
                else:
                    raise Exception('Oh no! You died!  Game over!')
                
        elif yes_or_no == 'No':
            delay_print('Ok! Come back when you are ready')
            return yes_or_no
            
            
        else:
            delay_print('You must reply Yes or No!')
            
        
     
            
    def move_map(self):
        delay_print('\n--Which direction would you like to move on the map?')
        map_move = ''
        #while map_move != 'exit':
        while map_move == '':
            #first if is when you are in town square tile
            #global map_array
            if self.map_array == [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][X][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]:
                delay_print('\n--Up = Arena, Left = Museum, Right = Market, Down = City Gates')
                map_move = input('\nDirection:  ')
                if map_move == 'Up':
                    self.map_array = [['[ ][ ][ ][ ][ ]'], ['[ ][ ][X][ ][ ]'], ['[ ][O][O][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]
                    return self.map_array
                elif map_move == 'Down':
                    self.map_array = [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][O][ ]'], ['[ ][ ][X][ ][ ]'], ['[ ][O][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]
                    return self.map_array
                elif map_move == 'Left':
                    self.map_array = [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][X][O][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]
                    return self.map_array
                elif map_move == 'Right':
                    self.map_array = [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][X][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]
                    return self.map_array
                else:
                    print('\nYou can\'t move in that direction from here!')
            #this elif is when you are at City Gates    
            elif self.map_array == [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][O][ ]'], ['[ ][ ][X][ ][ ]'], ['[ ][O][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]:
                delay_print('\nUp = Town Square, Down = Wilderness')
                map_move = input('\nDirection:  ')
                if map_move == 'Up':
                    self.map_array = [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][X][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]
                    return self.map_array
                elif map_move == 'Down':
                    self.map_array = [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][X][ ][ ]'], ['[ ][ ][ ][ ][ ]']]
                    return self.map_array
                else:
                    print('\nYou can\'t move in that direction from here!')
            #this elif is when you are at the Museum  
            elif self.map_array == [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][X][O][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]:
                delay_print('\nRight = Town Square')
                map_move = input('\nDirection:  ')
                if map_move == 'Right':
                    self.map_array = [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][X][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]
                    return self.map_array
                else:
                    print('\nYou can\'t move in that direction from here!')
            #this elif is when you are at the Market  
            elif self.map_array == [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][X][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]:
                delay_print('\nLeft = Town Square')
                map_move = input('\nDirection:  ')
                if map_move == 'Left':
                    self.map_array = [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][X][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]
                    return self.map_array 
                else:
                    print('\nYou can\'t move in that direction from here!')
            #this elif is when you are at the Arena  
            elif self.map_array == [['[ ][ ][ ][ ][ ]'], ['[ ][ ][X][ ][ ]'], ['[ ][O][O][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]:
                delay_print('\nDown = Town Square')
                map_move = input('\nDirection:  ')
                if map_move == 'Down':
                    self.map_array = [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][X][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]
                    return self.map_array
                else:
                    print('\nYou can\'t move in that direction from here!')
            #this elif is when you are at the Outskirts  
            elif self.map_array == [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][X][ ][ ]'], ['[ ][ ][ ][ ][ ]']]:
                delay_print('\nUp = City Gates, Left = Wilderness')
                map_move = input('\nDirection:  ')
                if map_move == 'Up':
                    self.map_array = [['[ ][ ][ ][ ][ ]'], ['[ ][ ][X][ ][ ]'], ['[ ][O][O][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]
                    return self.map_array
                elif map_move == 'Left':
                    self.map_array = [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][X][O][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]
                    return self.map_array
                else:
                    print('\nYou can\'t move in that direction from here!')
            #this elif is when you are in the Wilderness
            elif self.map_array == [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][X][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]:
                delay_print('\nRight = Outskirts')
                map_move = input('\nDirection:  ')
                if map_move == 'Right':
                    self.map_array = [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][X][ ][ ]'], ['[ ][ ][ ][ ][ ]']]
                    return self.map_array
                else:
                    print('\nYou can\'t move in that direction from here!')
            break
        
    def display_map(self):
        for i in self.map_array:
            for j in i:
                print(j,end = " ")
            print()
           
    def fight(self, Enemy):
        #allow two pokemon to fight each other
        #print the fight information
        delay_print(f'Prepare yourself!  A battle has begun between {self.name} and {Enemy.name}!\n')
        time.sleep(1)
        print(f'\n{self.name}')
        print('Element:', self.element)
        print('Damage:', self.damage)
        print('Toughness:', self.toughness)
        print('Level:', 3*(1+np.mean([self.damage,self.toughness]))) #calculate this however u want
        print('\nVS')
        print(f'\n{Enemy.name}')
        try:
            print('Type:', Enemy.species)
        except:
            print('Type:', Enemy.element)
        print('Damage:', Enemy.damage)
        print('Toughness:', Enemy.toughness)
        print('Level:', 3*(1+np.mean([Enemy.damage,Enemy.toughness]))) #calculate this however u want
        
        time.sleep(2)
        #display actual health bars based on class parameters:
        for i in range(int(self.health)):
            self.bars = self.bars + '='
        for i in range(int(Enemy.health)):
            Enemy.bars = Enemy.bars + '='
        
        #the actual loop for the fight itself, consider making its own function
        while (self.health > 0) and (Enemy.health > 0):
            #print the health of each pokemon
            print(f'\n{self.name}\tHP\t{self.health}\t{self.bars}')
            print(f'\n{Enemy.name}\tHP\t{Enemy.health}\t{Enemy.bars}')
            
            delay_print(f'\nOk {self.name}, stay frosty, and choose your next move:\n')
            time.sleep(0.5)
            for i, x in enumerate(self.abilities):
                print(f'{i+1}.', x)
            try:
                index = int(input('\nWhat\'ll it be? : '))
            except:
                delay_print('\nOops! That\'s not a valid entry, please enter a number between 1 and 4!')
                
            #or statements seemed to be causing me trouble so I'm writing out my if's for now - will need to investigate limitations of or
            if index == 4:
                delay_print(f'\n{self.name} used Health Potion!  Health is restored!')
            elif index == 3:
                delay_print(f'\n{self.name}\'s {self.abilities[index-1]} was used against {Enemy.name}!\n')
            elif index == 2:
                delay_print(f'\n{self.name}\'s {self.abilities[index-1]} was used against {Enemy.name}!\n')
            elif index == 1:
                delay_print(f'\n{self.name}\'s {self.abilities[index-1]} was used against {Enemy.name}!\n')
            else:
                delay_print(f'\nUh oh! That\'s not a valid entry. Please enter a number between 1 and 4!')  
            time.sleep(1)
            
            
            if index == 4:
                if int(self.health) < 25:
                    self.health = 25
                    self.bars = ''
                    for i in range(int(self.health)):
                        self.bars = self.bars + '='
                print(f'\n{self.name}\tHP\t{self.health}\t{self.bars}')
            else:
                #self_damage_determined = range(int(self.damage)) 
                self_damage_determined = random.randint(0, self.damage)
                if self_damage_determined == 0:
                    delay_print(f'\n{self.name}\'s {self.abilities[index-1]} missed!')
                else:
                    delay_print(f'\n{self.name}\'s {self.abilities[index-1]} did {self_damage_determined} damage to {Enemy.name}!')
                time.sleep(2)
                Enemy.health -= int(self_damage_determined)
                Enemy.bars = '' 
                for i in range(int(Enemy.health)):
                    Enemy.bars = Enemy.bars + '='
                    #new_enemy_health = Enemy.bars.replace('=', '', 1)
                    #Enemy.bars = new_enemy_health
                    #Enemy.bars = Enemy.bars + '='
            
            #check to see if Enemy died
            if Enemy.health <= 0:
                delay_print('\nYou did it!' + Enemy.name + ' is defeated!\n')
                break
            
            #Enemy's turn
            delay_print(f'\nNow for {Enemy.name} to have their turn, watch out!\n')
            for i, x in enumerate(Enemy.abilities):
                print(f'{i+1}.', x)
            index = random.choice(Enemy.abilities)
            delay_print(f'{Enemy.name} used {index}!\n')
            time.sleep(1)
            
            
            #determine damage!
            damage_determined = random.randint(0, Enemy.damage)
            if self_damage_determined == 0:
                delay_print(f'\n{Enemy.name}\'s {Enemy.abilities[index-1]} missed!')
            else:
                delay_print(f'\n{Enemy.name}\'s {Enemy.abilities[index-1]} did {damage_determined} damage to {self.name}!')
            time.sleep(2)
            self.health -= int(damage_determined)
            self.bars = ''
            for i in range(int(self.health)):
                self.bars = self.bars + '='
                #new_player_health = self.bars.replace('=', '', 1)
                #self.bars = new_player_health
                #self.bars = self.bars + '='
                
                
            time.sleep(1)
            # print(f'\n{self.name}\tHP\t{self.health}\t{self.bars}')
            # print(f'{Enemy.name}\tHP\t{Enemy.health}\t{Enemy.bars}\n')
            time.sleep(.5)
 
            # check to see if Player died
            if self.health <= 0:
                delay_print('\nOH NO! You Died!')
                raise Exception('\nGAME OVER')
                

#Create Enemy class      
class Enemy(Character):
    def __init__(self, name, species, abilities, stats, health, bars = ''):
        self.name = name
        self.species = species
        self.abilities = abilities
        self.damage = stats['Damage']
        self.toughness = stats['Toughness']
        self.health = health
        self.bars = bars  
        for i in range(health):
            bars = bars + '='