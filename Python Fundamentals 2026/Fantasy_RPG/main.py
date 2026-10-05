import random
import sys
from print_outs import PrintOuts

#Global variables
character_name = None
characters = []
inventory = []
death_state = False

class Weapon:
    def __init__(self, weapon, points):
        self.weapon = weapon
        self.points = points

class Character:
    def __init__(self, name, health, weapon, attack):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.attack = attack

    @classmethod
    def generate_character(cls):
        character_name = "Gen" + characters[random.randint(0,5)].name
        generated_weapon = characters[random.randint(0,5)].weapon
        print(f"Your character name is {character_name}, your weapon is {generated_weapon.weapon}, and your health is 100.\nMay the force be with you.")
        return {"character_name" : character_name, "health" : 50, "weapon" : generated_weapon.weapon, "damage" : generated_weapon.points, "attack" : "Moonlight Frost Breeze"}

    @classmethod
    def generate_opponent(cls):
        seed = random.randint(0,5)
        opponent = characters[seed].name 
        opponent_health = characters[seed].health
        opponent_damage = characters[seed].weapon.points
        opponent_attack = characters[seed].attack
        return {"opponent" : opponent, "opponent_health" :opponent_health, "opponent_damage" : opponent_damage, "opponent_attack" : opponent_attack}

    @classmethod
    def get_character_stats(cls, character_name):
        for character in characters:
            if character_name == character.name:
                return {"character_name" : character.name, "health" : character.health, "weapon" : character.weapon.weapon, "damage" : character.weapon.points, "attack" : character.attack}

    @classmethod
    def get_specific_opponent(cls, opponent_name = None):

        sorted_opponents = sorted(characters, key=lambda character : character.health)
        if opponent_name == "Gilgamesh":
            opponent = sorted_opponents[-1].name
            opponent_health = sorted_opponents[-1].health
            opponent_damage = sorted_opponents[-1].weapon.points
            opponent_attack = sorted_opponents[-1].attack
        else:
        # Take weakest opponent
            opponent = sorted_opponents[0].name
            opponent_health = sorted_opponents[0].health
            opponent_damage = sorted_opponents[0].weapon.points
            opponent_attack = sorted_opponents[0].attack
        return {"opponent" : opponent, "opponent_health" :opponent_health, "opponent_damage" : opponent_damage, "opponent_attack" : opponent_attack}

    @classmethod
    def get_inventory(cls):
        return [item for item in inventory]
    
    @classmethod
    def statistics(self, character_name):
        info = Character.get_character_stats(character_name)
        if info.get("character_name") is not None:
            print(f"\nCharacter name: {character_name}, character health: {info.get("health")}, character weapon: {info.get("weapon")}, Items in inventory: {self.get_inventory()}\n")
        else:
            print("Requested character not found. Please type the correct name.")

class CharacterActions():

    item_actions = {
        "Magic Shroom" : "shroom",
        "Lucky Charm" : "empowered",
        "Heal Potion" : "heal"
    }

    def attack(self, damage):
        return damage

    def dodge(self):
        print("Dodge")

    def initiate_hut_dialogue(self, character_name):
        PrintOuts.hut_dialogue("part 1")
        while True: # smithy dialogue
            player_answer = input()
            if "journey" in player_answer or "battle" in player_answer:
                PrintOuts.hut_dialogue("part 2")
                weapon_answer = input().upper()
                match weapon_answer:
                    case "Y":
                        self.update_character(character_name, "viking dagger")
                        break
                    case "N":
                        PrintOuts.hut_dialogue("part 3")
                        break # back to part three scenario.
                    case _:
                        print("Unknown input, please try again.")
            else:
                PrintOuts.hut_dialogue("part 4")
                break

    def use_inventory(self, character_name, user_choice, items_in_invetory):
        if items_in_invetory != []:
            if user_choice == "all":

                for item in items_in_invetory:
                    action = self.item_actions.get(item)
                    if action:
                        self.update_character(character_name, action)
            else:
                user_choice = self.item_actions.get(item)
                if action:
                    self.update_character(character_name, user_choice)
                else:
                    print("\nNothing could be used.")
        else:
            print("\nInvetory is empty, nothing can be used. Good luck!")

    def look_around(self, character_name, stage = None):
        
        match stage:
            case "1":
                seed = random.randint(0,100)
                if seed in range(35,55):
                    print("Congratulations. You have found a magic mushroom.")
                    inventory.append("Magic Shroom")
                else:
                    print("You did not find anything.")
            case "2":
                luck = random.randint(0,10) #5 hardcode to trigger
                if luck >= 5:
                    print("\nYou see, through this thick fog, just barely, that there is a hut. Shining inside is a dim light." \
                    "\nDo you proceed inside of it?  Y/N.")
                    choice = input().strip().upper()
                    match choice:
                        case "Y":
                            self.initiate_hut_dialogue(character_name)
                        case "N":
                            print("You move on.") # back to part three scenario.
                        case _: print("Please follow the predefined answers, Y or N.")

    #def use_ability(self, opponent):
        #print("Opponent is attacking with", character_attacks[opponent])
        # NOT USED YET

    def update_character(self, character_name, action, current_health = 0):
        #global characters
        for character in characters:
            if character_name == character.name:
                match action:
                    case "intoxication":
                        character.weapon.points -= 2
                    case "survived_battle":
                        character.health = current_health
                    case "resting":
                        if character.health != 100:
                            character.health = 100
                    case "heal":
                        if character.health != 100:
                            character.health += 15
                    case "empowered":
                        character.weapon.points += 10
                    case "remove":
                        characters.remove(character)
                    case "shroom":
                        character.weapon.points += 25
                        character.health += 25
                    case "viking dagger":
                        character.weapon.weapon = "Drengiligr"
                        character.weapon.points = 40
                        character.attack = "Piercing Vortex"

    def do_battle(self, character_name, opponent_stats, brutal_brawl = False, luck = 0):
        global death_state
        
        if luck > 4:
            self.update_character(character_name, "empowered")

        character_stats = Character.get_character_stats(character_name)
        print(f"\nAs the battle commences, you, {character_stats["character_name"]} are about to face off against {opponent_stats["opponent"]}")
        while True:
            print(f"\n{character_name} attacks with {character_stats["attack"]}")
            opponent_stats["opponent_health"] -= self.attack(character_stats["damage"])

            print("\nOpponent's turn.", opponent_stats["opponent"],"attacks with", opponent_stats["opponent_attack"])
            character_stats["health"] -= self.attack(opponent_stats["opponent_damage"])
            
            if opponent_stats["opponent_health"] < 0:
                print(f"\nAh.. I, {opponent_stats["opponent"]}, have been slain.. You have won...Farewell\n")
                print(f"################# VICTORY, BOW ME TO, YOU WORM ###################\n")
                if brutal_brawl is False:
                    self.update_character(opponent_stats["opponent"], "remove")
                    self.update_character(character_name, "survived_battle", character_stats["health"])
                break
            elif character_stats["health"] < 0: #bug, perhaps 
                print("\nThe brawl has ended. YOU DIED...\n")
                print(f"################ NO ONE CAN DEFEAT {opponent_stats["opponent"]} ###################\n" \
                      "\nYou must begin the game anew. Cleanup. Removing created character, clearing inventory, updting char stats.")
                self.update_character(character_name, "remove")
                #self.update_character(opponent_stats["opponent"], "resting") too OP?
                inventory.clear()
                death_state = True
                break
            print("\nYour health:", character_stats["health"], "opponent's health:", opponent_stats["opponent_health"])

class Story(CharacterActions):

    def brutal_brawl(self, character_name):
        print("Let's decide on an opponent!")
        opponent_stats = Character.generate_opponent()

        print(f"Your opponent is {opponent_stats["opponent"]} and the opponent's health is {opponent_stats["opponent_health"]}. Now brawl!")
        self.do_battle(character_name, opponent_stats, True)

    def story_part_one(self, character_name):
        # ################ Chapter 1. Treaturous Woods ################
        PrintOuts.story_one_print("part 1")
        while True: # story inner loop
            
            choice = input("Choose an option:\n").strip()
        
            if choice == "1":
                PrintOuts.story_one_print("part 3")
                while True: #inner conversation loop
                    first_q_a = input().strip()

                    if "church" in first_q_a or "explore" in first_q_a or "cathedral" in first_q_a or "exploration" in first_q_a:
                        PrintOuts.story_one_print("part 4")
                        break

                    elif "beverage" in first_q_a or "liquid" in first_q_a or "drink" in first_q_a:
                        PrintOuts.story_one_print("part 5")
                        second_q_a = input().strip().upper()
                        if second_q_a == "Y":
                            PrintOuts.story_one_print("part 6")
                            self.update_character(character_name, "intoxication")
                        else:
                            PrintOuts.story_one_print("part 7")
                            inventory.append("Lucky Charm")
                        break # escape from dialogue

                    else:
                        print("Sorry, not familiar with the your language. Please rephrase.")

            elif choice == "2":
                print("Going through the treaturous woods.")
                self.story_part_two(character_name)
                break
            else:
                print("\nInvalid input. Please select one of the options.")
            PrintOuts.story_one_print("part 2")

    def story_part_two(self, character_name):
        # ################ Chapter 2. City of the Forgotten Warriors ################
        global death_state
        PrintOuts.story_two_print("part 1")
        self.update_character(character_name, "empowered")
        
        PrintOuts.story_two_print("part 2")

        while True:
            choice = input().strip().lower()
            if choice == "left":
                PrintOuts.story_two_print("part 3")
                luck = int(input())
                opponent_stats = Character.generate_opponent()
                PrintOuts.story_two_print("part 4")
                self.do_battle(character_name, opponent_stats, False, luck)
                current_state_after_battle = Character.get_character_stats(character_name)

                if death_state:
                    break
                else:
                    print(f"\nYou have survived my tarnished. Your current health is {current_state_after_battle["health"]}." \
                            " Would you like to rest? Y/N?")
                    while True:
                        action = input().strip().upper()
                        match action:
                            case "Y": 
                                self.update_character(character_name, "resting")
                                current_state_after_battle = Character.get_character_stats(character_name) # refresh
                                break
                            case "N": 
                                print("You do not rest, you move on, like a true warrior.")
                                break
                            case _: print("Please follow the predefined answers, Y or N.")
                # check trigger        
                self.story_part_three(character_name)
                if death_state:
                    break

            elif choice == "right":
                PrintOuts.story_two_print("part 5")
                inventory.append("Heal Potion")
                
                action = input().strip().upper()
                match action:
                    case "Y": self.look_around(character_name, "1")
                    case "N": print("You do not look around, you move on.")
                    case   _: print("Please follow the predefined answers, Y or N.")
                self.story_part_three(character_name)
                if death_state:
                    PrintOuts.main_loop_print()
                    break
            else:
                print("Unknown input. Please type the word right or left.")

    def story_part_three(self, character_name):

        ################ Chapter 3. Final Act. ################
        global death_state
        PrintOuts.story_three_print("part 1")
        while True:
            PrintOuts.story_three_print("part 2")
            choice = input("\n").strip()
            match choice:
                case "1":
                    print("Being a fierce warrior, you proceed. as you approach the end of the rest, you spot a shadow of a person, or someone that resembles a person.")
                    opponent = Character.get_specific_opponent()
                    PrintOuts.story_three_print("part 3")
                    self.do_battle(character_name, opponent)
                    if death_state:
                        break
                    self.final_act(character_name) 
                case "2":
                    self.look_around(character_name, "2")
                case "3":
                    self.update_character(character_name, "resting")
                    print("\nYou have rested. Your health has been restored.")
                case "4":
                    Character.statistics(character_name)
                case _:
                    print("Unrecognized input. Please type in a number from 1 to 4.")

    def final_act(self, character_name):
        PrintOuts.final_act("part 1")
        while True:
            PrintOuts.final_act("part 2")
            choice = input("\n").strip()
            match choice:
                case "1":
                    print("Being a fierce warrior, you proceed. as you approach the end of the journey, you spot a shadow of a person, or someone that resembles a person.")
                    opponent = Character.get_specific_opponent("Gilgamesh")

                    PrintOuts.final_act("part 3")
                    self.do_battle(character_name, opponent)
                    if death_state:
                        print(f"\n################ Sadly, it is hard to beat King of Heroes, Gilgamesh. Better luck next time! ###################\n")
                    print("\n################ GAME OVER ################" \
                    "\n################ Thank you for playing, Ta Ta ################.")
                    sys.exit(-1)
                case "2":
                    print("\nHelp me please.")
                case "3":
                    Character.get_character_stats(character_name)
                case "4":
                    items = Character.get_inventory() # only used inventory for one person
                    print("Your current items in inventory are ", items, "Do you wish to use all of them or a specific one or none? Please type all, specific, or none.")
                    choice = input("\n").strip().lower()
                    if "all" in choice:
                        self.use_inventory(character_name, "all", inventory)
                    elif "specific" in choice:
                        print("You have in your invetory: ", Character.get_inventory(), "Which item do you want to use?")
                        choice = input("\n").strip()
                        self.use_inventory(character_name, choice, inventory)
                    elif "none" in choice:
                        print("\nNo items used, you proceed towards the final battle.")
                    else:
                        print("Please follow the predefined answers, all, none, specific.")
                case _:
                    print("Unrecognized input. Please type in a number from 1 to 4.")

#name, health, weapon, damage, attack
characters = [
    Character("Malenia", 75, Weapon("Katana", 20), "Waterfall Dance"),
    Character("Gilgamesh, A King amongst Kings", 200, Weapon("Sword", 22), "Look up and behold, Enuma Alish"),
    Character("Radahn", 125, Weapon("Dual Blades", 19), "Meteor Shower"),
    Character("Arthuria Pendragon", 100, Weapon("Chainsaw", 25), "Excalibur"),
    Character("Arlecchino", 70, Weapon("Spear", 20), "Puppet Dance"),
    Character("Laxasia", 50, Weapon("Sword", 22), "Mock Darkness")
]

def character_creation():
    global characters
    global character_name
    print("Would you like to have your own character and weapon? If yes, please click 1, if not, please click 2. This will pre-select a character for you.")
    while True:
        choice = input()
        if choice == "1":
            character_name = input("Character name:\n").strip()
            weapon = input("Character weapon\n").strip()
            # original weapon dmg = random.randint(1,100) 
            characters.append(Character(character_name, 100, Weapon(weapon, 30), "MegaWonk"))
            print(f"\nYour character name is {character_name}, your weapon is {weapon}, and your health is 100. \nMay the force be with you.\n")
            break
        elif choice == "2":
            character_stats = Character.generate_character()
            character_name = character_stats["character_name"]
            characters.append(Character(character_stats["character_name"], character_stats["health"], 
                Weapon(character_stats["weapon"], character_stats["damage"]), "Moonlight Frost Breeze"))
            break
        else:
            print("\nInvalid option. Please try again.")

def begin_rpg():
    story_object = Story()
    character_stats = None
    global death_state
    print("This is an action RPG game. Primary goal is NOT to die. However, opponents are tough. ")

    character_creation()

    while True:
        if death_state:
            character_creation()
            death_state = False
            continue
        PrintOuts.main_loop_print()
        choice = input("\nPlease select the desired option:\n").strip()

        if choice == "1":
            story_object.story_part_one(character_name)
        elif choice == "2":
            story_object.brutal_brawl(character_name)
        elif choice == "3":
            Character.statistics(character_name)
        elif choice == "X":
            print("Thank you for playing.")
            break
        else:
            print("\nInvalid option. Please try again.")

if __name__ == '__main__':
    begin_rpg()
