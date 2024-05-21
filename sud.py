import textwrap
import random
import sys

class Player:
    def __init__(self, name, character_type):
        """
        Initializes a new player object.

        Parameters:
        - name (str): The name of the player.
        - character_type (str): The type of character chosen by the player (e.g., "Elf", "Dwarf", "Orc").

        This method sets up the player's attributes such as name, character type, inventory, health, and attack power.
        Depending on the chosen character type, the player may start with specific items or abilities.
        """
        self.name = name
        self.character_type = character_type
        self.inventory = []  # Items carried by the player
        self.health = 100  # Initial health points
        self.attack = 10   # Initial attack power

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
        """
        Simulates the player casting a magic spell.

        This method generates a random amount of damage and prints a message indicating the damage dealt.
        """
        damage = random.randint(2, 7)
        print(f"{self.name} casts a magic spell, dealing {damage} damage!")
        # (This could interact with an enemy's health later)

    def bite(self):
        """
        Simulates the Orc's bite attack.

        This method is not implemented yet. It's intended to implement the logic for an Orc's bite attack.
        """
        print(f"{self.name} bites with sharp teeth!")
        # (This would need further logic to interact with enemies)

    def attack_enemy(self, enemy):
        """
        Initiates an attack against an enemy.

        Parameters:
        - enemy (str): The type of enemy being attacked (e.g., "rat").

        This method checks if the player has a weapon and attempts to attack the specified enemy.
        It returns True if the attack is successful, otherwise False.
        """
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
        """
        Initializes a new room object.

        Parameters:
        - name (str): The name of the room.
        - description (str): The description of the room.
        - items (list): Optional. The list of items present in the room.
        - exits (dict): Optional. The exits available from the room.

        This method sets up a new room with its name, description, items, and exits.
        """
        self.name = name
        self.description = description
        self.items = items if items else []  # Items present in the room
        self.exits = exits if exits else {}  # Exits available from the room

    def add_item(self, item):
        """
        Adds an item to the room.

        Parameters:
        - item (str): The name of the item to be added.

        This method adds the specified item to the list of items in the room.
        """
        self.items.append(item)

    def remove_item(self, item):
        """
        Removes an item from the room.

        Parameters:
        - item (str): The name of the item to be removed.

        This method removes the specified item from the list of items in the room.
        """
        if item in self.items:
            self.items.remove(item)

class Game:
    CHARACTER_TYPES = ["Elf", "Dwarf", "Human", "Orc"]

    def __init__(self):
        """
        Initializes a new game instance.

        This method sets up the game by initializing the player and current room attributes.
        """
        self.player = None  # The player object
        self.current_room = None  # The current room where the player is located

    def display_help(self):
        """
        Displays the help menu with available commands.

        This method prints out a list of commands that the player can use during the game.
        """
        print("=== Help Menu ===")
        print("Commands you can use:")
        print("'go [direction]': Move in the specified direction.")
        print("'take [item]': Take an item from the room.")
        print("'attack [target]': Attack an enemy in the room.")
        print("'inventory': Display your inventory.")
        print("'help': Display this help menu.")
        print("'quit': Quit the game.")

    def display_inventory(self):
        """
        Displays the player's inventory.

        This method prints out the items currently carried by the player.
        """
        print("=== Inventory ===")
        if not self.player.inventory:
            print("Your inventory is empty.")
        else:
            print("Items in your inventory:")
            for item in self.player.inventory:
                print("-", item)

    def use_item(self, item_name):
        """
        Allows the player to use an item from their inventory.

        Parameters:
        - item_name (str): The name of the item to be used.

        This method handles the usage of different items, such as food, drink, and weapons.
        It modifies player attributes accordingly (e.g., health, attack power) based on the item used.
        """
        if item_name == "food":
            # Increase player's health when eating food
            self.player.health += 20
            print("You ate some food. Your health has increased.")
            self.player.inventory.remove("food")
        elif item_name == "drink":
            # Increase player's health when drinking a drink
            self.player.health += 10
            print("You drank some refreshments. Your health has increased.")
            self.player.inventory.remove("drink")
        elif item_name == "old sword":
            if "old sword" in self.player.inventory:
                self.player.attack += 2
                print("You equipped the old sword. Your attack power has increased.")
            else:
                print("You don't have an old sword in your inventory.")
        else:
            print("You can't use that item.")

    def start(self):
        """
        Starts the adventure game.

        This method begins the game by prompting the player to enter their name and choose a character type.
        It then initializes the player object, sets up the game world, and starts the game loop.
        """
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
        """
        Sets up the game world with rooms and their connections.

        This method defines the rooms in the game world and their connections
        using exits. It also sets the starting room for the player.

        Players can add more rooms or modify existing ones to expand the game world.

        Rooms:
        - Open Field: An expansive field with exits leading to various locations.
        - Tavern: A cozy tavern where players can find food and drink.
        - Forest: A dense forest with tall trees and mysterious creatures.
        - Sea: The edge of a vast sea with crashing waves and seagulls.
        - Castle: A majestic castle filled with history and secrets.
        - Troll's Lair: A dark cave inhabited by trolls and danger.
        - Swamp: A murky swamp with foul-smelling air and croaking frogs.
        - Smithy: A small smithy where a blacksmith works tirelessly.

        Exits:
        - open_field: north (tavern), east (forest), west (sea), south (troll)
        - tavern: south (open_field)
        - forest: west (open_field), north (smithy)
        - sea: east (open_field)
        - troll: north (open_field)
        - swamp: north (forest)
        - smithy: south (forest)

        Starting Room: The starting room for the player is the Open Field.

        Items:
        - Tavern: Food and drink items are available for players to take.

        Lady Blacksmith:
        - The lady blacksmith resides in the smithy.
        - She presents players with a riddle to solve to earn an old sword.
        - The correct answer to her riddle is "pencil lead".
        """
        # Define rooms
        open_field = Room("Open Field", textwrap.fill("You are standing in an open field. You see a vast expanse of grass and the clear sky above you.", width=70))
        tavern = Room("Tavern", textwrap.fill("You enter a cozy tavern with the smell of food wafting through the air. Patrons are chatting and laughing at the tables.", width=70))
        forest = Room("Forest", textwrap.fill("You step into a dense forest. Tall trees loom overhead, and the air is thick with the scent of pine needles.", width=70))
        sea = Room("Sea", textwrap.fill("You arrive at the edge of a vast sea. Waves crash against the shore, and seagulls cry overhead.", width=70))
        castle = Room("Castle", textwrap.fill("Before you stands a majestic castle, its towers reaching towards the sky. A sense of grandeur and history surrounds the place.", width=70))
        troll = Room("Troll's Lair", textwrap.fill("You find yourself in a dark cave. The air is heavy with the stench of rot and decay.", width=70))
        swamp = Room("Swamp", textwrap.fill("You are in a murky swamp. The ground is soggy and foul-smelling, and you can hear the croaking of frogs nearby.", width=70))
        smithy = Room("Smithy", textwrap.fill("You enter a small smithy. The clang of metal on metal fills the air, and a blacksmith is busy at work in the north end of her shop.", width=70))

        # Define exits
        open_field.exits = {"north": tavern, "east": forest, "west": sea, "south": troll}
        tavern.exits = {"south": open_field}
        forest.exits = {"west": open_field, "north": smithy}
        sea.exits = {"east": open_field}
        troll.exits = {"north": open_field}
        swamp.exits = {"north": forest}
        smithy.exits = {"south": forest}

        # Set the starting room
        self.current_room = open_field

        # Set items in rooms if needed
        tavern.add_item("food")
        tavern.add_item("drink")

        # Add the lady blacksmith to the smithy
        blacksmith_question = "I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost every person. What am I?"
        blacksmith_response = "pencil lead"  # The correct answer
        blacksmith_item = "old sword"  # Item to be given if the answer is correct

        smithy.blacksmith_question = blacksmith_question
        smithy.blacksmith_response = blacksmith_response
        smithy.blacksmith_item = blacksmith_item

    def play(self):
        """
        Main game loop where the player interacts with the game world.

        This method displays current room information, handles player input,
        and executes corresponding actions based on the input.

        The player can move between rooms, take items, attack enemies, use items,
        view inventory, display help, or quit the game.

        Additional actions and functionality can be added here as needed.
        """
        while True:
            # Display current room information
            print("\n" + "=" * 20)
            print(f"You are in {self.current_room.name}")
            print(self.current_room.description)
            print("Exits:", ", ".join(self.current_room.exits.keys()))
            print("Items in the room:", ", ".join(self.current_room.items))

            # Check if the player is in the Smithy room
            if self.current_room.name == "Smithy":
                # Random chance to talk to the blacksmith
                if random.random() < 0.5:
                    self.talk_to_blacksmith()

            # Get user input
            command = input("Enter a command (e.g., 'go north', 'take knife'): ").lower()
            action = command.split()[0]

            if action == "go":
                direction = command.split()[1]
                self.go(direction)  # Call the go method to move the player
            elif action == "take":
                item = command.split()[1]
                self.take(item)  # Call the take method to pick up an item
            elif action == "attack":
                target = command.split()[1]
                self.attack(target)  # Call the attack method to attack an enemy
            elif action == "use":
                item = command.split()[1]
                self.use_item(item)  # Call the use_item method to use an item from the inventory
            elif action == "inventory":
                self.display_inventory()  # Call the display_inventory method to show the player's inventory
            elif action == "help":
                self.display_help()  # Call the display_help method to show the help menu
            elif action == "quit":
                self.quit_game()  # Call the quit_game method to exit the game
            # Add more actions here, like using items, attacking enemies, etc.
            # Ensure to handle invalid commands as well


    def quit_game(self):
        print("Thank you for playing! Exiting the game...")
        sys.exit()  # Exit the program

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
