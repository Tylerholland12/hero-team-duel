from hero import Hero, Ability, Team, Weapon, Armor


class Arena:
    def __init__(self):
        self.team_one = Team('Team one')
        self.team_two = Team('Team two')

    def create_ability(self):
        ability_name = input("Ability name: ")
        ability_damage = int(input("Ability damage: "))
        return Ability(ability_name, ability_damage)
    
    def create_weapon(self):
        weapon_name = input("Weapon name: ")
        weapon_damage = int(input("Weapon damage: "))
        return Weapon(weapon_name, weapon_damage)

    def create_armor(self):
        armor_name = input("Armor name: ")
        armor_num = int(input("Armor Amount: "))
        return Armor(armor_name, armor_num)

    def create_hero(self):
        hero_name = input("Hero name: ")
        hero_health = int(input("Hero starting health: "))
        new_hero = Hero(hero_name, hero_health)
        num_abilities = int(input("Number of desired abilities to add:"))
        for i in range(0, num_abilities):
            new_hero.add_ability(self.create_ability())
        num_weapons = int(input("Number of desired weapons to add:"))
        for i in range(0, num_weapons):
            new_hero.add_weapon(self.create_weapon())
        num_armor = int(input("Number of desired armors to add:"))
        for i in range(0, num_armor):
            new_hero.add_armor(self.create_armor())
            print(i)
        return new_hero

    def build_team_one(self):
        team_name = input("Enter a team name:")
        num_heroes = int(input("Enter number of heroes:"))
        self.team_one = Team(team_name)

        for i in range (0, num_heroes):
            self.team_one.heroes.append(self.create_hero())
        return i

    def build_team_two(self):
        team_name = input("Enter another team name: ")
        num_heroes = int(input("Enter number of heroes: "))
        self.team_two = Team(team_name)

        for i in range (0, num_heroes):
            self.team_two.heroes.append(self.create_hero())
        return i

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self):
        print(self.team_battle())


if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()