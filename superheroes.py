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
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        """ returns a random attack value between 1 and max_damage """
        #random number generator in range(0, max_damage)
        attack_val = random.randint(0, self.max_damage)
        return attack_val
    def update_attack(self, max_dmg):
        self.max_damage = max_dmg

class Weapon(Ability):
    def attack(self):
        weapon_damage = random.randint(self.max_damage//2, self.max_damage)
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
    def __init__(self, team_name):
        """Initiates the hero class with a team_name"""
        self.team_name = team_name
        self.heroes = list()
    def add_hero(self, hero):
        """ Adds a hero to the Team its called on"""
        self.heroes.append(hero)

    def revive_heroes(self, health = 100):
        for i in self.heroes:
            i.current_health = health

    def remove_hero(self, name):
        """Removes a Hero from the Team"""
        if name in self.heroes:
            i = self.heroes.index(name)
        else:
            return 0
        self.heroes.pop(i)
    def view_heroes(self):
        """Prints names of heroes on team"""
        print("Viewing {}'s Heroes: ".format(self.team_name))
        for i in self.heroes:
            print(i.name)

    def stats(self):
        """ Prints the ratio of kills/death for each memeber of the team"""
        for i in self.heroes:
            print('K/D is ' + i.kills/i.deaths)

    def attack(self):
        """Functions that itereates through the heroes in list and returns total attack damage """
        total_team_dmg = 0
        for i in self.heroes:
            total_team_dmg += i.attack()
        return total_team_dmg

class Arena:
    def __init__(self, name):
        self.name = name
        self.team_one = None
        self.team_two = None
    #### Figure out if another metod is needed for the hero build-out process
    # def hero_additions(self, addition_type, hero_name):
    #     """ allows for user to make additions to the hero. addition types include: abilities, armor, weapon, etc."""
    #     additions = []
    #     if self.yes_or_no

    def build_team_one(self):
        """Method builds out team one """
        team_name = input('Enter Team Name: ')
        new_team = Team(team_name)
        adding_heroes = True
        while adding_heroes:
            print('Adding heroes to you team...')
            new_hero_input(input('Enter New Hero Name or Enter "q" to quit: '))
            new_hero = Hero(new_hero_input)
            hero_ability_name = str(input('Give hero an ability: '))
            new_hero.add_ability(hero_ability_name)
            if new_hero.lower() == 'q':
                adding_heroes = False
            else:
                adding_heroes = True



    def build_team_two(self):
        """allows user to create team two  """

    def team_battle(self):
        """while loop for 2 teams to fight until all the heroes on one team are dead """

    def show_stats(self):
        """Prints all heroes in arena stats(k/d ratio) """


if __name__ == "__main__":
    fireball = Ability('fireball', 40)
    arena = Arena('Big Arena')
    arena.build_team_one()

    ##running this file from terminal will execute this block
    # snoop = Hero('Snoop Dogg')
    # snoop_ability = Ability('Smoke Cloud', 50)
    # snoop.add_ability(snoop_ability)
    # # print(snoop.attack())
    # willie = Hero('Willie Nelson')
    # hotbox = Ability('Hot Box', 2)
    # willie.add_ability(hotbox)
    # green_team = Team('Green Team')
    # green_team.add_hero(snoop)
    # green_team.view_heroes()
    # snoop.fight(willie)
    # willie.show_stats()
    # snoop.show_stats()
