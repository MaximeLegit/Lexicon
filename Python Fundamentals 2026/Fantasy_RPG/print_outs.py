
class PrintOuts():

    def main_loop_print():
        print("Now, let the quest begin! What would you like to do? Select the options that are of interest!"\
        "\n1. Begin Story" \
        "\n2. Brutal Brawl (Not for beginners!)" \
        "\n3. Show current character's statistics." \
        "\nX. Exit Game")

    def hut_dialogue(step):
        match step:
            case "part 1":
                print("A smithy is in the hut. She notices you. She asks you what are you doing in such an odd place?")
            case "part 2":
                print("Ah, you must be a warrior of great renown. As such, I can forge you a legendary dagger that was wielded by Ragnar himself. Would you like that? Y/N")
            case "part 3":
                print("No? I see. You have a decent weapon already.. You move on with your journey.")
            case "part 4":
                print("Well, seems you are not much of a talker, best be on yer way then.")

    def story_one_print(step):
        match step:
            case "part 1":
                print("\nWelcome to the game." \
                    "\nYou have several options to explore from. The story revolves around reaching the Carthia Cathedral, located at the West Valley." \
                    "\nIn order to get there, you need to find someone to speak to, to get information about the journey. " \
                    "Currently, you are located at the starting point in the city tavern." \
                    "\n\nWould you like to talk to the keep or go straight into the unknown?" \
                    "\n1. Talk to the keep\n2. Go straight into the unknown.")
            case "part 2":
                print("\nWould you like to talk to the keep again or go straight into the unknown?" \
                        "\n1. Talk to the keep\n2. Go straight into the unknown.")
            case "part 3":
                print("\nWell howdy there stranger, what brings you to these lands?")
            case "part 4":
                print("\nWell, as you know, you are currently in the capital's tavern. Legend has it that the fiercest warrior is located at the Carthia Cathedral, " \
                    "at the heart of the West Valley. \nThe road there goes through treaturous woods, city of the forgotten warriors, and the famous merridian bazar.")
            case "part 5":
                print("\nAh, well, I am aftraid the only liquid matter we have in this establishment is ale, would you like some? Y/N.")
            case "part 6":
                print("\nHere you go deary, on the house. Now, best be on your way to the west walley!")
            case "part 7":
                print("\nNo? Then best be on your way. Since you are a true warrior of unyielding faith, here is a lucky talisman for you." \
                "\nIt has been added to your inventory now.")

    def story_two_print(step):
        match step:
            case "part 1":
                print("\n################ Chapter 1. Treaturous Woods ################\n" \
                "\nAs you step into the woods, you are feeling very enforced, very strong ( even if you are not ).\nLegend has it that all new travellers get a blessing" \
                "from the lady of the woods, as to not to succumb to the dangers that lie ahead. You feel warmth.")
            case "part 2":
                print("\nAs you go along the woods, you see that the path diverges. You have a choice to make. Go left or go right. Please select accordingly.")
            case "part 3":
                print("\nAs you progress along the path to the left, you feel a chill in the air. You sense danger.. Lo and behold, your first opponent." \
                        "\nPlease type any number from 1 to 9. This ritual is done by the lady of the woods to help new travellers get accross safely.\n")
            case "part 4":
                print("\n################ Battle In the Treaturous Woods ################\n")
            case "part 5":
                print("Narrator:\nIt is always right to go right when the path is most definitely right. You see a healing potion, you relise that it will come in handy. You pick it up." \
                        "\nMy young tarnished. Thou art weary. Does thou wish to look around to see if you find something before you leave this forest? Y/N")

    def story_three_print(step):
        match step:
            case "part 1":
                print("\n################ Chapter 2. City of the Forgotten Warriors ################\n" \
                "\nYou have survived your first part of the journey. This city, the city of the forgotten warriors, is a an odd place. It is foggy, dark, and cold." \
                "\nThe sudden chill in your bones, you have felt it before, this unease, this forebodem before a battle. Knowing this, you have the following options:")
            case "part 2":
                print("\n1. Continue majestically, like the fearless person you are and see what awaits you." \
                "\n2. Look around" \
                "\n3. Rest" \
                "\n4. Show current character's statistics.")
            case "part 3":
                print("\n################ Battle in the City of the Forgotten Warriors ################\n")
    
    def final_act(step):
        match step:
            case "part 1":
                print("\n################ Chapter 3. Final Act ################\n" \
                "\nAs the story progresses, you know that someone grand will await you at the Cardia Cathedral. Now may be a good time to check if you have anything" \
                "useful in your inventory, heal up, say a prayer, or go forward like a true berserker and see what awaits you.")
            case "part 2":
                print("\n1. Proceed forward towards the final battle." \
                "\n2. Say a prayer." \
                "\n3. Get statistics." \
                "\n4. Use inventory items.")
            case "part 3":
                print("\n################ Final Battle ################\n")