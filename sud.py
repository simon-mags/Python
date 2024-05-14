import textwrap
import random

class Player:
    def __init__(self, name, character_type):
        self.name = name
        self.character_type = character_type
        self.inventory = []
        self.health = 100
        self.attack = 10  # Base attack power

        # Define starting items and abilities based on character type
        if character_type == "Elf":
            self.inventory.append("Magic Spell")
            self.special_ability = self.cast_magic_spell  # Assign a function for the ability
        elif character_type == "Dwarf":
            self.inventory.append("Hammer")
            self.attack += 5  # Increase attack for Dwarves
        elif character_type == "Orc":
            self.special_ability = self.bite  # Assign a function for the ability (not implemented yet)
            self.attack += 5

    def cast_magic_spell(self):
        # Generate a random damage amount between 2 and 6
        damage = random.randint(2, 7)
        print(f"{self.name} casts a magic spell, dealing {damage} damage!")
        # (This could interact with an enemy's health later)

    def bite(self):
        # Implement the logic for the Orc's bite attack (not implemented yet)
        print(f"{self.name} bites with sharp teeth!")
        # (This would need further logic to interact with enemies)

    def attack_enemy(self, enemy):
        if enemy == "rat":
            # Check if player has a weapon
            if "knife" in self.inventory:
                print("You attack the rat with your knife!")
                if random.random() < 0.5:  # 50% chance of success
                    print("You defeat the rat!")
                    self.attack += 1  # Increase attack points
                    return True
                else:
                    print("The rat dodges your attack!")
                    return False
            else:
                print("You need a weapon to attack!")
                return False
        else:
            print("There's no such target here.")
            return False

class Room:
    def __init__(self, name, description, items=None, exits=None):
        self.name = name
        self.description = description
        self.items = items if items else []
        self.exits = exits if exits else {}

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

class Game:
    CHARACTER_TYPES = ["Elf", "Dwarf", "Human", "Orc"]

    def __init__(self):
        self.player = None
        self.current_room = None

    def start(self):
        print("Welcome to the Adventure Game!")
        player_name = input("Enter your name: ")
        character_type = self.choose_character_type()
        self.player = Player(player_name, character_type)
        # You can add more character setup here (e.g., based on character type)

        self.setup_world()

        # Start the game loop
        self.play()

    def choose_character_type(self):
        print("Choose your character type:")
        for i, character_type in enumerate(self.CHARACTER_TYPES, start=1):
            print(f"{i}. {character_type}")
        while True:
            choice = input("Enter the number of your choice: ")
            if choice.isdigit() and 1 <= int(choice) <= len(self.CHARACTER_TYPES):
                return self.CHARACTER_TYPES[int(choice) - 1]
            else:
                print("Invalid choice. Please enter a number between 1 and", len(self.CHARACTER_TYPES))


    def setup_world(self):
        # Define your rooms and their connections here
        # Open Field
        open_field = Room("Open Field", textwrap.fill("You are standing in an open field. You see a vast expanse of grass and the clear sky above you.", width=70))
        # Tavern
        tavern = Room("Tavern", textwrap.fill("You enter a cozy tavern with the smell of food wafting through the air. Patrons are chatting and laughing at the tables.", width=70))
        # Forest
        forest = Room("Forest", textwrap.fill("You step into a dense forest. Tall trees loom overhead, and the air is thick with the scent of pine needles.", width=70))
        # Sea
        sea = Room("Sea", textwrap.fill("You arrive at the edge of a vast sea. Waves crash against the shore, and seagulls cry overhead.", width=70))
        # Castle
        castle = Room("Castle", textwrap.fill("Before you stands a majestic castle, its towers reaching towards the sky. A sense of grandeur and history surrounds the place.", width=70))
        # Troll
        troll = Room("Troll's Lair", textwrap.fill("You find yourself in a dark cave. The air is heavy with the stench of rot and decay.", width=70))
        # Swamp
        swamp = Room("Swamp", textwrap.fill("You are in a murky swamp. The ground is soggy and foul-smelling, and you can hear the croaking of frogs nearby.", width=70))

        # Define exits
        open_field.exits = {"north": tavern, "east": forest, "west": sea, "south": troll}
        tavern.exits = {"south": open_field}
        forest.exits = {"west": open_field}
        sea.exits = {"east": open_field}
        troll.exits = {"north": open_field}
        swamp.exits = {"north": forest}

        # Set the starting room
        self.current_room = open_field

        # Set items in rooms if needed
        tavern.add_item("food")
        tavern.add_item("drink")

        # Add the lady blacksmith to the open field
        blacksmith_question = "A blacksmith makes horse shoes. If the blacksmith has 5 iron bars, and each horse shoe requires 2 iron bars, how many horse shoes can the blacksmith make?"
        blacksmith_response = "3"  # The correct answer
        blacksmith_item = "old sword"  # Item to be given if the answer is correct

        open_field.blacksmith_question = blacksmith_question
        open_field.blacksmith_response = blacksmith_response
        open_field.blacksmith_item = blacksmith_item

    def play(self):
        while True:
            # Display current room information
            print("\n" + "=" * 20)
            print(f"You are in {self.current_room.name}")
            print(self.current_room.description)
            print("Exits:", ", ".join(self.current_room.exits.keys()))
            print("Items in the room:", ", ".join(self.current_room.items))

            # Check if the player is in the Open Field and talk to the lady blacksmith
            if self.current_room == "Open Field":
                self.talk_to_blacksmith()

            # Get user input
            command = input("Enter a command (e.g., 'go north', 'take knife'): ").lower()
            action = command.split()[0]

            if action == "go":
                direction = command.split()[1]
                self.go(direction)
            elif action == "take":
                item = command.split()[1]
                self.take(item)
            elif action == "attack":
                target = command.split()[1]
                self.attack(target)
            # Add more actions here, like using items, attacking enemies, etc.
            # Ensure to handle invalid commands as well

    def talk_to_blacksmith(self):
        print("You see a lady blacksmith nearby.")
        response = input("Would you like to talk to her? (yes/no): ").lower()
        if response == "yes":
            print("The lady blacksmith asks you a question.")
            print(self.current_room.blacksmith_question)
            answer = input("Enter your answer: ")
            if answer == self.current_room.blacksmith_response:
                print("Congratulations! You answered correctly.")
                print("The lady blacksmith gives you an old sword.")
                self.player.inventory.append(self.current_room.blacksmith_item)
            else:
                print("Sorry, that's incorrect. Try again later.")

    def attack(self, target):
        if target == "rat" and "rat" in self.current_room.items:
            success = self.player.attack_enemy(target)
            if success:
                self.current_room.remove_item("rat")
        else:
            print("There's no such target here.")

    def go(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
        else:
            print("You can't go that way.")

    def take(self, item_name):
        if item_name in self.current_room.items:
            self.player.inventory.append(item_name)
            self.current_room.remove_item(item_name)
            print(f"You took the {item_name}.")
        else:
            print("There's no such item here.")

def main():
    # Create a new game instance
    game = Game()
    # Start the game
    game.start()

if __name__ == "__main__":
    # This block will only be executed if the script is run directly,
    # not if it's imported as a module in another script
    main()
