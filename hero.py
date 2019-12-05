import random

class Ability:
    def __init__(self, name, attack_strength):
        '''
        Initialize the values passed into this
        method as instance variables.
        '''

        # Assign the "name" and "max_damage"
        # for a specific instance of the Ability class
        self.name = name
        # self.max_damage = 100
        self.attack_strength = attack_strength

    def attack(self):
        ''' Return a value between 0 and the value set by
        self.attack_strength.
        '''

        # Pick a random value between 0 and self.attack_strength
        random_value = random.randint(0, self.attack_strength)
        print(self.name + " attack of " + str(random_value))
        return random_value

class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        # TODO: Create instance variables for the values passed in.
        self.name = name
        self.max_block = max_block

    def block(self):
        '''
        Return a random value between 0 and the
        initialized max_block strength.
        '''
        block_attack = random.randint(0, self.max_block)
        return block_attack

class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer
          kills: Integer
          deaths: Integer
      '''
    # abilities and armors don't have starting values,
    # and are set to empty lists on initialization
        self.abilities = []
        self.armors = []
        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health
        # Update the constructor for Hero class to track deaths and kills
        self.deaths = 0
        self.kills = 0

    def __str__(self):
        '''string conversion method'''
        return self.name

    def add_ability(self, ability):
        ''' Add ability to abilities list 
        '''

        # We used the append method to add strings to a list
        # in the Rainbow Checklist tutorial. This time,
        # we're not adding strings, instead we'll add ability objects.
        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
          return: total_damage:Int
      '''
        # start our total out at 0
        print("--attack method called--")
        total_damage = 0
        # loop through all of our hero's abilities
        for each in self.abilities:
            # add the damage of each attack to our running total

            total_damage += each.attack()
            print("Total Damage is " + str(total_damage))
        # return the total damage
        return int(total_damage)

    def add_armor(self, armor):
        '''Add armor to self.armors
        Armor: Armor Object
        '''
        self.armors.append(armor)

    def defend(self):
        '''Calculate the total block amount from all armor blocks.
        return: total_block:Int
        '''
    # TODO: This method should run the block method on each armor
    # in self.armors
        defense = 0
        # initializes the defense variable
        # which stores the accumated values of all block actions
        if len(self.armors) > 0:
            for each_armor in self.armors:
                defense += each_armor.block()
            print(f"Armor blocks " + str(defense) + " points of damage")
            return defense
        else:
            return 0

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        defense = self.defend()
        self.current_health -= damage - defense

    def is_alive(self):
        '''Check current_health. If less than or equal to zero, return
        False. Otherwise return True
        '''
        
        if self.current_health <= 0:
            return False
        else:
            return True

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities
        '''
       
        self.abilities.append(weapon)

    def add_kill(self, num_kills):
        ''' Update self.kills by num_kills amount
        '''
        self.kills += num_kills

    def add_death(self, num_deaths):
        ''' Update deaths with num_deaths
        '''
        self.deaths += num_deaths

    def fight(self, opponent):
        '''Current Hero will take turns fighting an opponent hero
        '''
        
        while self.is_alive() and opponent.is_alive():
            if self.abilities == opponent.abilities:
                # declare a draw if combatant abilities are equivalent
                print("No winner possible")
                print("Draw")
           
            # attack opponent
            damage = self.attack()
           
            # accumulate opponent's damage
            opponent.take_damage(damage)
          
            # be attacked by opponent
            damage = opponent.attack()
          
            # be attacked by opponent
            self.take_damage(damage)

        if self.current_health > 0:
            print(self.name + " is the winner!")
            self.add_kill(1)
            opponent.add_death(1)
        else:
            print(opponent.name + " is the winner!")
            self.add_death(1)
            opponent.add_kill(1)

class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        # TODO: Use integer division to find half of the max_damage value
        # then return a random integer between
        # half of max_damage and max_damage
        print("max damage of " + self.name + " is ")
        print(str(self.attack_strength))
        min_damage = self.attack_strength // 2
        weapon_attack_value = random.randint(min_damage, self.attack_strength)
        return weapon_attack_value

class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name and an empty list of heroes
        '''
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        ''' Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        foundHero = False
        # loop through each hero in our list
        for hero in self.heroes:
            # if we find them, remove them from the list
            if hero.name == name:
                self.heroes.remove(hero)
                # set our indicator to True
                foundHero = True
        # if we looped through our list and did not find our hero,
        # the indicator would have never changed, so return 0
        if not foundHero:
            return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        for hero in self.heroes:
            print(hero)

    def add_hero(self, hero):
        '''Add hero to self.heroes'''
        self.heroes.append(hero)

    def stats(self):
        '''print team stats'''
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print("{} Kill/Deaths:{}".format(hero.name, kd))

    def revive_heroes(self):
        ''' Reset all heroes health to starting_health'''
        # TODO: for each hero in self.heroes,
        # set the hero's current_health to their starting_health
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        # added team arg
        ''' Battle each team against each other.'''

        living_heroes = list()
        living_opponents = list()
        # changed list() to team and other_team

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            # TODO: Complete the following steps:
            # Randomly select a living hero from each team (√)
            random_living_hero = random.choice(living_heroes)
            random_living_opponent = random.choice(living_opponents)
            # have the heroes fight each other (√)
            random_living_hero.fight(random_living_opponent)
            # update the list of living_heroes and living_opponents
            # to reflect the result of the fight (√)
            status = hero.is_alive()
            if random_living_hero.is_alive():
                living_opponents.remove(random_living_opponent)
            else:
                living_heroes.remove(random_living_hero)


