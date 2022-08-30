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
    def __init__(self, name, element, abilities, stats, health, coins, potions, bars = '', map_array = [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][X][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']] ):
        self.name = name
        self.element = element
        self.abilities = abilities
        self.damage = stats['Damage']
        self.toughness = stats['Toughness']
        self.coins = coins
        self.potions = potions
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
        global ganger
        global radioactiveBear
        global check_health
        global chosen_element
      
        
        chosen_element = ''
        while chosen_element != ('Water' or 'Fire' or 'Earth' or 'Air'):
            chosen_element = input('\nChoose Element:  ')
            self.element = chosen_element
            if chosen_element == ('Earth'):
                delay_print('Aha! an ' + chosen_element + ' Elemancer!  Good, good, we\'ve been short on those.')
                fireElemancer = Character('Blazen', 'Fire Elemancer', ['Rain of Fire', 'Ignite', 'Turn to Cinders'], {'Damage': 10, 'Toughness': 8}, 20, 0, 0)
                fireElemancer.damage = fireElemancer.damage * 1.5
                waterElemancer = Character('Misty', 'Water Elemancer', ['Hydro Blast', 'Ice Spear', 'Drowning Waves'], {'Damage': 10, 'Toughness': 9}, 20, 0, 0)
                airElemancer = Character('Zephyr', 'Air Elemancer', ['Lightning Coil', 'Whirlwind', 'Crushing Pressure'], {'Damage': 10, 'Toughness': 7}, 20, 0, 0)
                airElemancer.damage = airElemancer.damage / 1.5
                self.abilities = ['Turn to Stone', 'Summon Rock Elemental', 'Razor Vines', 'Health Potion']
                ganger = Enemy('Ganger', 'Traitorous Gang Member', ['Stab','Kick','Pistol Shot','Grenade'], {'Damage': 8, 'Toughness': 10}, 15)
                radioactiveBear = Enemy('Radioactive Bear', 'Mutated Animal', ['Bite', 'Acid Spit', 'Claw'], {'Damage': 9, 'Toughness': 8}, 30)
                check_health = [radioactiveBear.health, ganger.health, airElemancer.health, waterElemancer.health, fireElemancer.health]
                break
            elif chosen_element == ('Air'):
                delay_print('Aha! an ' + chosen_element + ' Elemancer!  Good, good, we\'ve been short on those.')
                fireElemancer = Character('Blazen', 'Fire Elemancer', ['Rain of Fire', 'Ignite', 'Turn to Cinders'], {'Damage': 10, 'Toughness': 8}, 20, 0, 0)
                waterElemancer = Character('Misty', 'Water Elemancer', ['Hydro Blast', 'Ice Spear', 'Drowning Waves'], {'Damage': 10, 'Toughness': 9}, 20, 0, 0)
                waterElemancer.damage = waterElemancer.damage / 1.5
                earthElemancer = Character('Brock', 'Earth Elemancer', ['Turn to Stone', 'Summon Rock Elemental', 'Razor Vines'], {'Damage': 10, 'Toughness': 7}, 20, 0, 0)
                earthElemancer.damage = earthElemancer.damage * 1.5
                self.abilities = ['Lightning Coil', 'Whirlwind', 'Crushing Pressure', 'Health Potion']
                ganger = Enemy('Ganger', 'Traitorous Gang Member', ['Stab','Kick','Pistol Shot','Grenade'], {'Damage': 8, 'Toughness': 10}, 15)
                radioactiveBear = Enemy('Radioactive Bear', 'Mutated Animal', ['Bite', 'Acid Spit', 'Claw'], {'Damage': 9, 'Toughness': 8}, 30)
                check_health = [radioactiveBear.health, ganger.health, fireElemancer.health, waterElemancer.health, earthElemancer.health]
                break
            elif chosen_element == ('Fire'):
                delay_print('Aha! a ' + chosen_element + ' Elemancer!  Good, good, we\'ve been short on those.')
                waterElemancer = Character('Misty', 'Water Elemancer', ['Hydro Blast', 'Ice Spear', 'Drowning Waves'], {'Damage': 10, 'Toughness': 9}, 20, 0, 0)
                waterElemancer.damage = waterElemancer.damage * 1.5
                earthElemancer = Character('Brock', 'Earth Elemancer', ['Turn to Stone', 'Summon Rock Elemental', 'Razor Vines'], {'Damage': 10, 'Toughness': 10}, 20, 0, 0)
                earthElemancer.damage = earthElemancer.damage / 1.5
                airElemancer = Character('Zephyr', 'Air Elemancer', ['Lightning Coil', 'Whirlwind', 'Crushing Pressure'], {'Damage': 10, 'Toughness': 7}, 20, 0, 0)
                self.abilities = ['Rain of Fire', 'Ignite', 'Turn to Cinders', 'Health Potion']
                ganger = Enemy('Ganger', 'Traitorous Gang Member', ['Stab','Kick','Pistol Shot','Grenade'], {'Damage': 8, 'Toughness': 10}, 15)
                radioactiveBear = Enemy('Radioactive Bear', 'Mutated Animal', ['Bite', 'Acid Spit', 'Claw'], {'Damage': 9, 'Toughness': 8}, 30)
                check_health = [radioactiveBear.health, ganger.health, airElemancer.health, waterElemancer.health, earthElemancer.health]
                break
            elif chosen_element == ('Water'):
                delay_print('Aha! a ' + chosen_element + ' Elemancer!  Good, good, we\'ve been short on those.')
                airElemancer = Character('Zephyr', 'Air Elemancer', ['Lightning Coil', 'Whirlwind', 'Crushing Pressure'], {'Damage': 10, 'Toughness': 7}, 20, 0, 0)
                airElemancer.damage = airElemancer.damage * 1.5
                earthElemancer = Character('Brock', 'Earth Elemancer', ['Turn to Stone', 'Summon Rock Elemental', 'Razor Vines'], {'Damage': 10, 'Toughness': 10}, 20, 0, 0)
                fireElemancer = Character('Blazen', 'Fire Elemancer', ['Rain of Fire', 'Ignite', 'Turn to Cinders'], {'Damage': 10, 'Toughness': 8}, 20, 0, 0)
                fireElemancer.damage = fireElemancer.damage / 1.5
                self.abilities = ['Hydro Blast', 'Ice Spear', 'Drowning Waves', 'Health Potion']
                ganger = Enemy('Ganger', 'Traitorous Gang Member', ['Stab','Kick','Pistol Shot','Grenade'], {'Damage': 8, 'Toughness': 10}, 15)
                radioactiveBear = Enemy('Radioactive Bear', 'Mutated Animal', ['Bite', 'Acid Spit', 'Claw'], {'Damage': 9, 'Toughness': 8}, 30)
                check_health = [radioactiveBear.health, ganger.health, airElemancer.health, fireElemancer.health, earthElemancer.health]
                break
            else:
                delay_print('Hmmm, that\'s not a valid Element, try again!\n')
                
    def win_condition(self):
        if chosen_element == ('Earth'):
            check_health = [radioactiveBear.health, ganger.health, airElemancer.health, waterElemancer.health, fireElemancer.health]
        elif chosen_element == ('Air'):
            check_health = [radioactiveBear.health, ganger.health, fireElemancer.health, waterElemancer.health, earthElemancer.health]
        elif chosen_element == ('Fire'):
            check_health = [radioactiveBear.health, ganger.health, airElemancer.health, waterElemancer.health, earthElemancer.health]
        elif chosen_element == ('Water'):
            check_health = [radioactiveBear.health, ganger.health, airElemancer.health, fireElemancer.health, earthElemancer.health]
        else:
            pass
            
        # for i in check_health:
            # print(i)
            
        if max(check_health) <= 0:         #max(check_health)
            delay_print('You win the game!')
            raise Exception('You Win!')
        # global check_health
        # if max(check_health) <= 1:
            
        else:
            pass
    
    def museum_event(self):
        delay_print('You walk into the museum.  Looking around you can see exhibits and people viewing them.\n')
        delay_print('A Museum Curator approaches you.\n')
        delay_print('Curator:  You there!  Are you...you are!  An Elemancer! Welcome!\n')
        delay_print('The Curator is clearly excited to have a modern example of what much of the History here is about\n')
        delay_print('Curator:  Please, come come, may I interest you in a tour?\n')
        yon = 'x'
        while yon != 'y':
            print('-------WARNING - THIS IS JUST LONG EXPOSITION AND YOU CANNOT SKIP IT ONCE YOU BEGIN--------')
            yon = input('Would you like to go on a tour of the Museum?  Yes / No:  \n')
            if yon == 'Yes':
                delay_print('Curator:  Fantastic!  Follow me!  I will fill you in on our history here as we pass each exhibit!\n')
                delay_print('')
                delay_print('Referred to as the “Kala Kala” or more simply “Kala” by Humans, the Kala\'Arakashir (Kah-Lah Arih-Kesheer)\n') 
                delay_print('are a prideful, hunter-gatherer race that was introduced to the Earth in the year 2136.  Their home planet\n') 
                delay_print('is located in the Human database under: Planet 1024-CR-23, but it is commonly known among Kala as \n') 
                delay_print('“Izz\'hanakir,” directly translating to “Mother Home,” but more specifically meaning “Place to be born or \n') 
                delay_print('raised.”  The Kala do not have means of space travel, and were brought to Earth originally as slaves by the\n') 
                delay_print('Grand Empire.  It wasn\'t until the great uprising and the corresponding wars that the Kala were freed by \n') 
                delay_print('Rebels and began to take a stand for their race.\n') 
                delay_print('The Kala fought closely alongside Rebels, and understood that they were very different from the Humans who \n') 
                delay_print('enslaved them.  Over decades of constant chaos and slaughter, the Rebels and the Kala regularly put their \n') 
                delay_print('lives in danger to save one another, and a fellowship was born.  There was always a clear understanding that \n') 
                delay_print('both parties warred for nothing short of total peace and freedom.  As the years dragged on, it became clear \n') 
                delay_print('to the Rebels and the Kala that when everything was ended, there would be little chance of ever returning \n') 
                delay_print('the Kala to their home-world, at least for an age.  This bonded the Humans and Kala all the more, as they \n') 
                delay_print('knew the world they were fighting for would have to be shared for years to come.\n') 
                delay_print('Kala live for upwards of 600 years, whereas Humans live around 180 years, rarely spanning longer than 250.  \n') 
                delay_print('Many Humans have chosen Kala as their children\'s godparents, as the same Kala can be a parent and a mentor \n') 
                delay_print('for up to 3 Human generations.  This correspondence has allowed for very deep and long-lasting relationships \n') 
                delay_print('between the two races.  It is rare for Humans and Kala to choose each other as mates, generally because \n') 
                delay_print('there is no way for the two races to sexually interact, let alone conceive.  However, some individuals \n') 
                delay_print('choose to have such relationships, solely for the emotional experience, and it is not frowned upon by most. \n') 
                delay_print('Kala society is very much based around hunting tribes.  Small, tight knit bands of Kala live together on \n') 
                delay_print('Izz\'hanakir, using their incredible hunting prowess to survive and live comfortably.  Honor and pride are \n') 
                delay_print('strong contenders for what is considered success in their culture.  Power and respect are earned through \n') 
                delay_print('one\'s ability to hunt. \n') 
                delay_print('The women in Kala culture are not necessarily the “care-takers,” but rather are hunters as well.  Housework \n') 
                delay_print('and the like is typically done by children.  This makes for generally symmetrical lives for men and women, \n') 
                delay_print('and therefore, two mates are not as socially bound as they are in Human culture.  However, Kala partners are \n') 
                delay_print('sexually loyal, and do not engage sexually with other Kala once they have completed Izz\'banatir.\n') 
                delay_print('The Kala, as well as much of the wildlife on Izz\'hanakir, do not have a bone structure like Humans and other \n') 
                delay_print('vertebrates.  Instead of solid bone, they have a skeleton built with small organic sacks.  These sacks can \n') 
                delay_print('reactively reduce or increase their air pressure, allowing for incredible flexibility when moving.  When at \n') 
                delay_print('full pressure levels, the sacks have enough tensile strength to be comparable to bone, but if the creature \n') 
                delay_print('needs to move in an abnormal way, they are able to because the sacks can let out air and allow for more \n') 
                delay_print('flexibility.  This structure also allows Kala to perform incredible jumps.  In the air, the sacks deflate, \n') 
                delay_print('and as the Kala lands, the sacks increase pressure to counteract the force of the ground against their legs, \n') 
                delay_print('like thousands of little airbags.\n') 
                delay_print('Curator: Well, that about covers everything on the Kala.  Come back another time to explore the Great War!\n')
                break
                
            elif yon == 'No':
                delay_print('Curator: Bah, what a shame. Come back any time!\n')
                break
            else:
                delay_print('--Please enter Yes or No!\n')
                continue
        
                   
    
    def wilderness_event(self):
        if radioactiveBear.health <= 0:
            self.move_map()
        else:
            delay_print('Feeling tough, are we?\n')
            delay_print('You walk into the thick forest, dense and mysterious as it may be.\n')
            time.sleep(2)
            delay_print('As you walk, dry sticks and leaves crack like thunder beneath your feet\n')
            time.sleep(1.5)
            delay_print('Anxiety builds in you as you sense you\'re being watched.....stalked.\n')
            delay_print('Breath through the nostrils of something....big....just came from behind you.\n')
            self.fight(radioactiveBear)
            delay_print('The mutant beast falls at your feet, its final breath launched from its snout.')
            #get Dragon Pickaxe

    
    def outskirts_event(self):
        if ganger.health <= 0 and radioactiveBear.health <= 0:
            delay_print('You pass by the dead Ganger on your way back. His corpse has stopped twitching.')
            return
        elif ganger.health <= 0:
            delay_print('Phew!  You survived the ambush!  Nice work!\n')
            delay_print('If you want to head back to town, you can, but you won\'t get your pay!\n')
            delay_print('If you still feel up to it, head into the forest to finish your quest!\n')
            return    
        else:
            delay_print('As the city gates close behind you, you hear the Guardsman shout:\n') # UPDATE THIS TO INSIDE THE FUNCTION SO IT DOESNT PLAY ON REPEAT VISIT
            delay_print('Be warned, young Elemancer, going out solo has its dangers, even for the likes of you!\n')
            delay_print('His voice trails off --\n')
            time.sleep(2)
            delay_print('Ahhhh, the great outdoors.  You stride forward with a lightness in your step.\n')
            delay_print('As you look out, you see a meadow leading to a dense forest.\n')
            delay_print('There is a path leading outward from the City Gates.\n')
            delay_print('You can choose to take the path, or walk through the dense meadow.\n')

        rep = 'x'
        while rep != 'y':
            rep = input('Head out along the path, or cut through the meadow?: Path / Meadow: \n')
            if rep == 'Path':
                delay_print('You set out on the path.  The sun glints in your eye, blinding you for a moment.\n')
                delay_print('There is some rustling in the bushes nearby, you are almost certain of it\n')
                delay_print('Hmm, it must have been a fox or something.  Your pace picks back up\n')
                delay_print('You\'re nearing the forest.  Better start thinking about wha---\n')
                delay_print('Ganger: \"HEY YOU! YOU\'RE IN REAL TROUBLE NOW!!\"\n')
                delay_print('You should have trusted your gut! You were followed by a rogue Ganger!\n')
                self.fight(ganger)
                delay_print('The Ganger collapses, you look around, but it seems like he was alone.\n')
                break
            elif rep == 'Meadow':
                delay_print('You venture into the tall foliage, it\'s almost up to your neck!\n')
                delay_print('Some of the boulders around here are nearly 10 feet tall.\n')
                delay_print('Starting to doubt why exactly you chose this route, you continue to trudge forward\n')
                delay_print('The forest is getting close.  Time to start thinking abou-----\n')
                delay_print('A rogue Ganger jumps out from behind a boulder --\n')
                delay_print('Ganger: \"HEY YOU! YOU\'RE IN REAL TROUBLE NOW!!\"\n')
                self.fight(ganger)
                delay_print('The Ganger collapses, you look around, but it seems like he was alone.')
                break
            else:
                delay_print('Please enter either Path or Meadow.\n')
                continue
                
        
        
    def citygates_event(self):
        if radioactiveBear.health <= 0 and ganger.health <= 0 and self.coins == 0:
            delay_print('You\'re back!  Excellent!  How was the scouting mission?\n')
            delay_print('A Ganger you say!?  Those scum always skulking about.\n')
            delay_print('Wait, AND a radioactive mutant bear?  You\'ve had quite the day then!\n')
            delay_print('Well then, you\'ll be wanting this - you earned it!\n')
            self.coins = 100
            delay_print('--Guardsman hands you 100 gold coins--\n')
            delay_print('Alright then, off with ye.  Head back into town where its safe!\n')
        elif radioactiveBear.health <= 0 and ganger.health <= 0 and self.coins > 0:
            delay_print('Oi!  You\'ve got no business left here!  Move along now!\n')
        elif radioactiveBear.health > 0 and ganger.health <= 0:
            delay_print('I saw you kill that wretched Ganger. Nice work! But your quest isn\'t over!\n')
        else:
            delay_print('Guardsman: Oi there!  You look pretty strong, care to lend a hand?\n')
            delay_print('--You approach the Guardsman to hear him out.\n')
            delay_print('Guardsman: We\'re short on men today, can I get ye to go scout the area? I\'ll pay ye for ye troubles!\n')
            answ = ''
            while answ != 'x':
                delay_print('--Warning-- Heading out of the City Gates is dangerous, be prepared with Health Potions!\n')
                answ = input('Accept the Guardsman\'s quest?  Yes / No:  \n')
                if answ == 'Yes':
                    delay_print('You nod at the Guardsman.\n')
                    delay_print('Make your way to the Outskirts!\n')
                    break
                elif answ == 'No':
                    delay_print('You shake your head at the Guardsman and turn away.\n')
                    delay_print('In that case, head back to the Town Square!\n')
                    break
                else:
                    delay_print('Please answer Yes or No!\n')
                    continue
        time.sleep(1.5)
        
    def market_event(self):
        delay_print('\nMerchant: You there!  Could I interest you in my wares?\n')
        delay_print('--Would you like to approach the Merchant?  It appears he is selling Potions!\n')
        first_resp = ''
        while first_resp != 'x':
            first_resp = input('Yes or No:  \n')
            if first_resp == 'Yes':
                delay_print('You approach the Merchant, cautious but unconcerned.\n')
                break
            elif first_resp == 'No':
                delay_print('Alright then, head back to town.\n')
                break
            else:
                delay_print('Please enter either Yes or No.\n')
                continue
        if first_resp == 'No':
            return
        else:
            pass
        
        delay_print('Merchant:  Well then, you look like an Elemancer.  You could probably use some Health Potions, no?\n')
        resp = ''
        while resp != 'x':
            resp = input('Would you like to purchase 20 Potions for 100 Gold Pieces? Yes / No:  \n')
            if resp == 'Yes':
                if self.coins == 0:
                    delay_print('--Oh no!  You don\'t have enough coins!\n')
                    delay_print('Merchant:  Taking me for a fool, eh!  Piss off!\n')
                    delay_print('--You leave the Merchant\'s area before trouble brews\n')
                    break
                else:
                    delay_print('Merchant:  Excellent!  That\'ll be 100 Gold Coins!\n')
                    delay_print('--You hand over the coins. The Merchant counts them meticulously.\n')
                    delay_print('--After inspecting your coinage, the Merchant, almost reluctantly, hands you 20 Health Potions.\n')
                    delay_print('--You leave the Merchant\'s area, prepared and ready to do battle!\n')
                    self.coins = 0
                    self.potions += 20
                    break
            elif resp == 'No':
                delay_print('Merchant:  Well alright, be on your way then! --The Merchant then utters something under his breath\n')
                delay_print('--You leave the Merchant\'s area before trouble brews\n')
            else:
                delay_print('Oops!  That\'s not a valid response, please enter Yes or No\n')
                continue
 
        time.sleep(1.5)

                
    def arena_gauntlet(self):
        delay_print('Welcome to the Arena!  Here you will fight through a gauntlet of fellow Elemancers\n')
        delay_print('in a series of Trials. Should you defeat each of the Elemancers with whom you do not\n')
        delay_print('share the same Element, you will be declared victorious!\n')
        delay_print('Would you like to begin the Trial now, or come back later?\n')
        delay_print('!!!!!!>Hint: You will want plenty of Health Potions<!!!!!!!\n')
        delay_print('!!!!!!!!!!!!>They are available in the Market<!!!!!!!!!!!!!\n')
        yes_or_no = ''
        while yes_or_no != ('Yes' or 'No'):
            yes_or_no = input('Start Trial Now?  Yes / No: ')
            if yes_or_no == 'Yes':
                while self.health > 0:
                    if self.element == ('Earth'):
                        self.fight(airElemancer)
                        time.sleep(3)
                        self.fight(waterElemancer)
                        time.sleep(3)
                        self.fight(fireElemancer)
                        delay_print('Congratulations!  You have passed your Trial and defeated the Gauntlet!')
                        break
                        
                    elif self.element == ('Air'):
                        self.fight(waterElemancer)
                        time.sleep(3)
                        self.fight(fireElemancer)
                        time.sleep(3)
                        self.fight(earthElemancer)
                        delay_print('Congratulations!  You have passed your Trial and defeated the Gauntlet!')
                        break
                        
                    elif self.element == ('Fire'):
                        self.fight(earthElemancer)
                        time.sleep(3)
                        self.fight(airElemancer)
                        time.sleep(3)
                        self.fight(waterElemancer)
                        delay_print('Congratulations!  You have passed your Trial and defeated the Gauntlet!')
                        break
                        
                    elif self.element == ('Water'):
                        self.fight(fireElemancer)
                        time.sleep(3)
                        self.fight(earthElemancer)
                        time.sleep(3)
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
            mistake_map = ''
            while mistake_map != 'x':
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
                        continue
                #this elif is when you are at City Gates    
                elif self.map_array == [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][O][ ]'], ['[ ][ ][X][ ][ ]'], ['[ ][O][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]:
                    delay_print('\nUp = Town Square, Down = Outskirts')
                    map_move = input('\nDirection:  ')
                    if map_move == 'Up':
                        self.map_array = [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][X][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]
                        return self.map_array
                    elif map_move == 'Down':
                        self.map_array = [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][X][ ][ ]'], ['[ ][ ][ ][ ][ ]']]
                        return self.map_array
                    else:
                        print('\nYou can\'t move in that direction from here!')
                        continue
                #this elif is when you are at the Museum  
                elif self.map_array == [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][X][O][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]:
                    delay_print('\nRight = Town Square')
                    map_move = input('\nDirection:  ')
                    if map_move == 'Right':
                        self.map_array = [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][X][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]
                        return self.map_array
                    else:
                        print('\nYou can\'t move in that direction from here!')
                        continue
                #this elif is when you are at the Market  
                elif self.map_array == [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][X][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]:
                    delay_print('\nLeft = Town Square')
                    map_move = input('\nDirection:  ')
                    if map_move == 'Left':
                        self.map_array = [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][X][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]
                        return self.map_array 
                    else:
                        print('\nYou can\'t move in that direction from here!')
                        continue
                #this elif is when you are at the Arena  
                elif self.map_array == [['[ ][ ][ ][ ][ ]'], ['[ ][ ][X][ ][ ]'], ['[ ][O][O][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]:
                    delay_print('\nDown = Town Square')
                    map_move = input('\nDirection:  ')
                    if map_move == 'Down':
                        self.map_array = [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][X][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]
                        return self.map_array
                    else:
                        print('\nYou can\'t move in that direction from here!')
                        continue
                #this elif is when you are at the Outskirts  
                elif self.map_array == [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][X][ ][ ]'], ['[ ][ ][ ][ ][ ]']]:
                    delay_print('\nUp = City Gates, Left = Wilderness')
                    map_move = input('\nDirection:  ')
                    if map_move == 'Up':
                        self.map_array = [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][O][ ]'], ['[ ][ ][X][ ][ ]'], ['[ ][O][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]
                        return self.map_array
                    elif map_move == 'Left':
                        self.map_array = [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][X][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]
                        return self.map_array
                    else:
                        print('\nYou can\'t move in that direction from here!')
                        continue
                #this elif is when you are in the Wilderness
                elif self.map_array == [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][X][O][ ][ ]'], ['[ ][ ][ ][ ][ ]']]:
                    delay_print('\nRight = Outskirts')
                    map_move = input('\nDirection:  ')
                    if map_move == 'Right':
                        self.map_array = [['[ ][ ][ ][ ][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][O][O][ ]'], ['[ ][ ][O][ ][ ]'], ['[ ][O][X][ ][ ]'], ['[ ][ ][ ][ ][ ]']]
                        return self.map_array
                    else:
                        print('\nYou can\'t move in that direction from here!')
                        continue
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
        print('Level:', 3*(1+np.mean([self.damage,self.toughness]))) #toughness just used to calc level now
        print('\nVS')
        print(f'\n{Enemy.name}')
        try:
            print('Element:', Enemy.element)
        except:
            print('Type:', Enemy.species)
        print('Damage:', Enemy.damage)
        print('Toughness:', Enemy.toughness)
        print('Level:', 3*(1+np.mean([Enemy.damage,Enemy.toughness]))) #toughness just used to calc level now
        
        time.sleep(2)
        #display actual health bars based on class parameters:
        self.bars = ''
        Enemy.bars = ''
        for i in range(int(self.health)):
            self.bars = self.bars + '='
        for i in range(int(Enemy.health)):
            Enemy.bars = Enemy.bars + '='
        
        #the actual loop for the fight itself, consider making its own function
        while (self.health > 0) and (Enemy.health > 0):
            #print the health 
            
            if len(self.name) > 6 and (len(Enemy.name) > len(self.name) + 4):
                print(f'\n{self.name}\tHP\t{self.health}\t{self.bars}')
            else:
                print(f'\n{self.name}\t\tHP\t{self.health}\t{self.bars}')   
            if len(Enemy.name) > 6:
                print(f'\n{Enemy.name}\tHP\t{Enemy.health}\t{Enemy.bars}')
            else:
                print(f'\n{Enemy.name}\t\tHP\t{Enemy.health}\t{Enemy.bars}')
            
            delay_print(f'\nOk {self.name}, stay frosty, and choose your next move:\n')
            time.sleep(0.5)
            for i, x in enumerate(self.abilities):
                print(f'{i+1}.', x)
                
            index = ''    
            while index != ('1' or '2' or '3' or '4'):    
                index = input('\nWhat\'ll it be? : ')
                try:
                    new_index_again = int(index)
                except:
                    delay_print(f'\nUh oh! That\'s not a valid entry. Please enter a number between 1 and 4!')
                    continue 
                if index == '4':
                    if self.potions == 0:
                        delay_print('You don\'t have any Health Potions!')
                        continue
                    else:
                        delay_print(f'\n{self.name} used Health Potion!  Health is restored!')
                        break
                elif index == '3':
                    delay_print(f'\n{self.name}\'s {self.abilities[new_index_again-1]} was used against {Enemy.name}!\n')
                    break
                elif index == '2':
                    delay_print(f'\n{self.name}\'s {self.abilities[new_index_again-1]} was used against {Enemy.name}!\n')
                    break
                elif index == '1':
                    delay_print(f'\n{self.name}\'s {self.abilities[new_index_again-1]} was used against {Enemy.name}!\n')
                    break
                else:
                    delay_print(f'\nUh oh! That\'s not a valid entry. Please enter a number between 1 and 4!\n')
                    continue  
            
            time.sleep(1) 
            
            if index == '4':
                if self.potions == 0:
                    pass
                elif int(self.health) <= 25:
                    self.potions -= 1
                    self.health = 25
                    self.bars = ''
                    for i in range(int(self.health)):
                        self.bars = self.bars + '='
                print(f'\n{self.name}\tHP\t{self.health}\t{self.bars}')
            else:
                #self_damage_determined = range(int(self.damage)) 
                self_damage_determined = random.randint(0, self.damage)
                new_index = int(index)
                if self_damage_determined == 0:
                    delay_print(f'\n{self.name}\'s {self.abilities[new_index-1]} missed!')
                else:
                    delay_print(f'\n{self.name}\'s {self.abilities[new_index-1]} did {self_damage_determined} damage to {Enemy.name}!')
                time.sleep(2)
                Enemy.health -= int(self_damage_determined)
                Enemy.bars = '' 
                for i in range(int(Enemy.health)):
                    Enemy.bars = Enemy.bars + '='
                    
            
            #check to see if Enemy died
            if Enemy.health <= 0:
                delay_print('\nYou did it! ' + Enemy.name + ' is defeated!\n')
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
            if damage_determined <= 0:
                delay_print(f'\n{Enemy.name}\'s {index} missed!')
            else:
                delay_print(f'\n{Enemy.name}\'s {index} did {damage_determined} damage to {self.name}!')
            time.sleep(2)
            self.health -= int(damage_determined)
            self.bars = ''
            for i in range(int(self.health)):
                self.bars = self.bars + '='
                
                
                
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