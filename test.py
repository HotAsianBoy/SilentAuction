class Player:
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.inventory = []

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"You picked up {item.name}.")

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Game:
    def __init__(self):
        self.player = None
        self.create_game()

    def create_game(self):
        # Define rooms
        room1 = Room("Room 1", "You are in a small room.")
        room2 = Room("Room 2", "You find yourself in a dark corridor.")
        room3 = Room("Room 3", "A large hall opens up before you.")

        # Define exits
        room1.add_exit("east", room2)
        room2.add_exit("west", room1)
        room2.add_exit("east", room3)
        room3.add_exit("west", room2)

        # Define items
        key = Item("Key", "A shiny golden key.")
        room1.add_item(key)

        # Set starting room
        self.player = Player("Player")
        self.player.current_room = room1

    def play(self):
        print("Welcome to the Complex Python Text Adventure Game!")
        print("Type 'help' for a list of commands.")

        while True:
            print("\n" + self.player.current_room.name)
            print(self.player.current_room.description)

            command = input("Enter your command: ").lower()

            if command == "quit":
                print("Thanks for playing! Goodbye.")
                break
            elif command == "help":
                print("Commands: look, go [direction], inventory, pick up [item], quit")
            elif command == "look":
                self.look_around()
            elif command.startswith("go "):
                direction = command[3:]
                self.go(direction)
            elif command.startswith("pick up "):
                item_name = command[8:]
                self.pick_up(item_name)
            elif command == "inventory":
                self.show_inventory()
            else:
                print("Invalid command. Type 'help' for a list of commands.")

    def look_around(self):
        print("Exits:", ", ".join(self.player.current_room.exits.keys()))
        print("Items in the room:", ", ".join(item.name for item in self.player.current_room.items))

    def go(self, direction):
        if direction in self.player.current_room.exits:
            next_room = self.player.current_room.exits[direction]
            self.player.current_room = next_room
            print("You go", direction + ".")
        else:
            print("You can't go that way.")

    def pick_up(self, item_name):
        current_room = self.player.current_room
        for item in current_room.items:
            if item.name.lower() == item_name.lower():
                self.player.add_to_inventory(item)
                current_room.remove_item(item)
                return
        print(f"No {item_name} found in the room.")

    def show_inventory(self):
        if not self.player.inventory:
            print("Your inventory is empty.")
        else:
            print("Your inventory:", ", ".join(item.name for item in self.player.inventory))


# Run the game
if __name__ == "__main__":
    game = Game()
    game.play()
