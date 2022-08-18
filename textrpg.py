import time
import numpy as np
import sys

#Delay Printing (borrowed from StackOverflow)

def delay_print(s):
    #print one character at a time
    #https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
   
   
#Create Player class
class Character:
    #definte init function - this sets the initial state of the Character class.  Basically
    #this is just defininig the properties we're going to generate for each Character.
    def __init__(self, name, element, abilities, stats, health, bars = ''):
        self.name = name
        self.element = element
        self.abilities = abilities
        self.damage = stats['Damage']
        self.toughness = stats['Toughness']
        self.bars = bars
        self.health = health
           
    def fight(self, Enemy):
        #allow two pokemon to fight each other
        #print the fight information
        delay_print(f'Prepare yourself!  A battle has begun between {self.name} and {Enemy.name}!')
        time.sleep(1)
        print(f'\n{self.name}')
        print('Element:', self.element)
        print('Damage:', self.damage)
        print('Toughness:', self.toughness)
        print('Level:', 3*(1+np.mean([self.damage,self.toughness]))) #calculate this however u want
        print('\nVS')
        print(f'\n{Enemy.name}')
        print('Type:', Enemy.species)
        print('Damage:', Enemy.damage)
        print('Toughness:', Enemy.toughness)
        print('Level:', 3*(1+np.mean([Enemy.damage,Enemy.toughness]))) #calculate this however u want
        
        time.sleep(2)
        #display actual health bars based on class parameters:
        for i in range(self.health):
            self.bars = self.bars + '='
        for i in range(Enemy.health):
            Enemy.bars = Enemy.bars + '='
        
        #the actual loop for the fight itself, consider making its own function
        while (self.health > 0) and (Enemy.health > 0):
            #print the health of each pokemon
            print(f'\n{self.name}\t\HP\t{self.bars}')
            print(f'\n{Enemy.name}\t\HP\t{Enemy.bars}\n')
            
            delay_print(f'Ok {self.name}, stay frosty, and choose your next move:')
            time.sleep(0.5)
            for i, x in enumerate(self.moves):
                print(f'{i+1}.', x)
            index = int(input('What\'ll it be? : '))
            delay_print(f'{self.name}\'s {self.moves[index-1]} was used against {Enemy.name}!')
            time.sleep(1)

#Create Enemy class      
class Enemy:
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

    
    
    
    
    
    
    
    
    
    
#still unsure why - but standard procedure in python (at least for OOP) is to add:
if __name__ == '__main__':
    Tyler = Character('Tyler', 'Fire Elemancer', ['kickpunch','punchkick','scream','jump'], {'Damage': 4, 'Toughness': 7}, 25)
    Zombie = Enemy('Zombie', 'Undead', ['gargle','groan','barf','punch'], {'Damage': 3, 'Toughness': 10}, 10)
    
    Tyler.fight(Zombie)