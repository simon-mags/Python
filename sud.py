class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        # You can add more attributes for the player, such as health, skills, etc.

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
    def __init__(self):
        self.player = None
        self.current_room = None

    def start(self):
        print("Welcome to the Adventure Game!")
        player_name = input("Enter your name: ")
        self.player = Player(player_name)
        # You can add more character setup here

        self.setup_world()

        # Start the game loop
        self.play()

    def setup_world(self):
        # Define your rooms and their connections here
        # Example:
        room1 = Room("Living Room", "You are in a cozy living room.", items=["knife"], exits={"north": room2})
        room2 = Room("Kitchen", "You are in a kitchen with a big stove.", exits={"south": room1})

        # Set the starting room
        self.current_room = room1

    def play(self):
        while True:
            # Display current room information
            print("\n" + "=" * 20)
            print(f"You are in {self.current_room.name}")
            print(self.current_room.description)
            print("Exits:", ", ".join(self.current_room.exits.keys()))
            print("Items in the room:", ", ".join(self.current_room.items))

            # Get user input
            command = input("Enter a command (e.g., 'go north', 'take knife'): ").lower()
            action = command.split()[0]

            if action == "go":
                direction = command.split()[1]
                self.go(direction)
            elif action == "take":
                item = command.split()[1]
                self.take(item)
            # Add more actions here, like using items, attacking enemies, etc.
            # Ensure to handle invalid commands as well

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

# Start the game
game = Game()
game.start()
