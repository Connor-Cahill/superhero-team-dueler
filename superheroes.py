import random

class Hero:
    def __init__(self, name, health = 100):
        """ The init functions for hero class, gives hero a name and sets starting health equal to 100"""
        self.name = name
        self.starting_health = health
        self.current_health = health
        self.abilities = list()
        self.armors = list()
        self.kills = 0
        self.deaths = 0

    def add_ability(self, ability):
        """Adds abilities to the abilities list"""
        self.abilities.append(ability)

    def add_armor(self, armor):
        """Adds Armor to hero's armor list"""
        self.armors.append(armor)

    def attack(self):
        """Calculates damage from list of abilities. """
        total_attack_dmg = 0
        for i in self.abilities:
            total_attack_dmg += i.attack()
        return total_attack_dmg

    def take_damage(self, dmg):
        """ Updates self.current_health with the damage passed through"""
        self.current_health -= ( dmg - self.defend() )
        if self.current_health < 0:
            self.deaths += 1
        return self.current_health

    def defend(self):
        """runs the block function on every piece of armor hero has and returns that as the total_block_val """
        total_block_val = 0
        for i in self.armors:
            total_block_val += i.block()
        return total_block_val

    def is_alive(self):
        """Returns True is hero is alive and False if the hero is dead"""
        if self.current_health > 0:
            return True
        else:
            print('{} died'.format(self.name))
            return False


    def add_kill(self, num_kills):
        """Adds kill to hero"""
        self.kills += num_kills

    def fight(self, opponent):
        """Runs loop to attack opponent until someone dies"""
        print('{} will be fighting {}'.format(self.name, opponent.name))
        while(self.is_alive() == True and opponent.is_alive() == True):
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
            if opponent.is_alive() == False:
                self.kills += 1
            print('fighting ... ')

    def show_stats(self):
        """Prints heros K/D ratio"""
        print(self.kills)
        print(self.deaths)
        if self.deaths > 0:
            kd_ratio = self.kills/self.deaths
        else:
            kd_ratio = self.kills
        print("{} K/D Ratio: {}".format(self.name, kd_ratio))

class Ability:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    def attack(self):
        """ returns a random attack value between 1 and strength """
        #random number generator in range(0, strength)
        attack_val = random.randint(0, self.strength)
        return attack_val

    def update_attack(self, new_dmg):
        """Allows user to update attack damage of ability """
        self.strength = new_dmg

class Weapon(Ability):
    def attack(self):
        weapon_damage = random.randint(self.strength//2, self.strength)
        return weapon_damage
class Armor:
    def __init__(self, name, max_block):
        """ Creates armor instance with name and max block value"""
        self.name = name
        self.max_block = max_block
    def block(self):
        """Generates a random number between 0 and max_block and returns as block value """
        block_val = random.randint(0, self.max_block)
        return block_val


class Team:
    def __init__(self, name):
        """Initiates the hero class with a name"""
        self.name = name
        self.heroes = list()

    def add_hero(self, hero):
        """ Adds a hero to the Team its called on"""
        self.heroes.append(hero)

    def revive_heroes(self, health = 100):
        """Iterates through heroes on team and sets their health back to 100(default starting health) """
        for i in self.heroes:
            i.current_health = health

    def remove_hero(self, name):
        """Removes a Hero from the Team"""
        index = self.find_hero(name)
        if index == -1:
            return 0
        self.heroes.pop(index)

    def view_all_heroes(self):
        """Prints names of heroes on team"""
        print("Viewing {}'s Heroes: ".format(self.name))
        for i in self.heroes:
            print(i.name)


    def find_hero(self, name):
        """Find index of specific hero on a team """
        hero_index = -1
        for index, hero in enumerate(self.heroes):
            if hero.name == name:
                hero_index = index
        return hero_index

    def stats(self):
        """ Prints the ratio of kills/death for each memeber of the team"""
        for i in self.heroes:
            i.show_stats()

    def attack(self, other_team):
        """Selects a random alive hero from your team and opposite team and sets them to fight each other until one dies """
        while len(self.alive_heroes()) > 0 and len(other_team.alive_heroes()) > 0:
            random_hero1 = random.choice(self.alive_heroes())
            random_hero2 = random.choice(other_team.alive_heroes())
            ##make the randomly selected alive heroes fight
            random_hero1.fight(random_hero2)

    def update_kills(self, kills):
        """Updates a heroes kill count for kills made in team battles """
        for hero in self.heroes:
            hero.add_kill(kills)


    def alive_heroes(self):
        """Makes a list of alive heroes from team """
        alive_heroes = []
        for hero in self.heroes:
            if hero.is_alive():
                alive_heroes.append(hero)
            return alive_heroes


    def defend(self, dmg_amount):
        """Takes the sum of all heroes in Team class and returns that as the defend value of Team """
        defense_strength = sum([hero.defend() for hero in self.heroes])
        excess_dmg = dmg_amount - defense_strength
        if excess_dmg > 0:
            return self.take_damage(excess_dmg)
        return 0
    ##I dont think I need this 
    # def take_damage(self, dmg):
    #     """Takes damage from input and deals that to the team  """
    #     dmg = dmg / len(self.heroes)
    #     dead_heroes = 0
    #     for hero in self.heroes:
    #         hero.take_damage(dmg)
    #         if hero.current_health <= 0:
    #             dead_heroes += 1
    #     return dead_heroes



class Arena:
    def __init__(self, name):
        self.name = name
        self.team_one = None
        self.team_two = None




    def build_team(self):
        name = input('Enter a team name: ')
        new_team = Team(name)
        keep_adding_heroes = True
        while keep_adding_heroes:
            print('Adding a hero to {}...'.format(name))
            new_hero = Hero(input('Enter the name of the hero: '))
            new_hero.abilities = self.hero_additions('ability', new_hero.name)
            new_hero.abilities = self.hero_additions('weapon', new_hero.name)
            new_hero.armors = self.hero_additions('armor', new_hero.name)
            new_team.add_hero(new_hero)
            keep_adding_heroes = self.yes_or_no('Would you like to keep adding heroes to {}? Answer ( y/n ): '.format(name))
        return new_team

    def yes_or_no(self, message):
        """Method that returns false and will end a loop when user input n, will return True if user inputs y """
        user_res = input(message)
        if user_res.lower() == 'y':
            return True
        elif user_res.lower() == 'n':
            return False
        else:
            print('Input not recognized')
        return self.yes_or_no(message)

    def hero_additions(self, addition_type, hero_name):
        """Method that allows users to make additions to heros while building out the team (using Arena methods) """
        adds = []
        if self.yes_or_no('do you want to add {} to {}? answer( y/n ): '.format(addition_type, hero_name)):
            keep_asking = True
            addition = Ability if addition_type =='ability' else Weapon if addition_type == 'weapon' else Armor
            while keep_asking:
                name = input('What is this {} called?'.format(addition_type))
                block_or_attack = 'block' if addition_type == Armor else 'attack'
                strength = int(input("What is {}'s  {} strength?".format(name, block_or_attack)))
                adds.append(addition(name, strength))
                keep_asking = self.yes_or_no('Do you want to add another {}? Answer ( y/n ): '.format(addition_type))
            return adds


    def build_team_one(self):
        """Method builds out team one """
        print('Building team one ....')
        self.team_one =  self.build_team()
        return self.team_one


    def build_team_two(self):
        """allows user to create team two  """
        print('Building team two ...')
        self.team_two = self.build_team()
        return self.team_two

    # def team_battle(self):
    #     """ while loop for 2 teams to fight until all the heroes on one team are dead """
    #     while self.team_one.still_alive() and self.team_two.still_alive():
    #         self.team_one.attack(self.team_two)
    #         self.team_two.attack(self.team_one)
    #         if self.team_one.still_alive():
    #             print('{} wins the battle!'.format(self.team_one.name))
    #             self.team_one.update_kills(len(self.team_two.heroes))
    #             return False
    #         else:
    #             print('{} wins the battle!'.format(self.team_two.name))
    #             self.team_two.update_kills(len(self.team_one.heroes))
    #             return False

    def team_battle(self):
        """ While team 1 and team 2 have living heroes they will fight. While loop will break when one team has no living hereos left."""
        print('Team Battle Starting...')
        while self.team_one.alive_heroes() and self.team_two.alive_heroes():
            self.team_one.attack(self.team_two)
            self.team_two.attack(self.team_one)
            if self.team_one.alive_heroes():
                print('{} wins this battle.'.format(self.team_one.name))
                self.team_one.update_kills(len(self.team_two.heroes))
                return False
            else:
                print('{} wins this battle.'.format(self.team_two.name))
                self.team_two.update_kills(len(self.team_one.heroes))
                return False



    def show_stats(self):
        """ Prints all heroes in arena stats(k/d ratio) """
        print('Printing stats')
        self.team_one.stats()
        self.team_two.stats()


if __name__ == "__main__":
    arena = Arena('Big Arena')
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()





    ##running this file from terminal will execute this block
    # snoop = Hero('Snoop Dogg')
    # snoop_ability = Ability('Smoke Cloud', 50)
    # snoop.add_ability(snoop_ability)
    # # # print(snoop.attack())
    # willie = Hero('Willie Nelson')
    # hotbox = Ability('Hot Box', 2)
    # willie.add_ability(hotbox)
    # # green_team = Team('Green Team')
    # # green_team.add_hero(snoop)
    # # green_team.view_heroes()
    # snoop.fight(willie)
    # print(snoop.kills)
    # print(willie.deaths)
    # willie.show_stats()
    # snoop.show_stats()
