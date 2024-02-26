import time

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

class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.inventory = []

    def move(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
            print("You move to", self.current_room.name)
            print(self.current_room.description)
        else:
            print("You cannot go that way.")

    def take_item(self, item_name):
        for item in self.current_room.items:
            if item.name.lower() == item_name.lower():
                self.inventory.append(item)
                self.current_room.remove_item(item)
                print("You take the", item_name)
                return
        print("There is no", item_name, "here.")

    def check_inventory(self):
        if self.inventory:
            print("Inventory:")
            for item in self.inventory:
                print("-", item.name)
        else:
            print("Your inventory is empty.")

def main():
    # Define rooms
    living_room = Room("Living Room", "You are in a spacious living room.")
    kitchen = Room("Kitchen", "You find yourself in a cozy kitchen.")
    bedroom = Room("Bedroom", "This is a comfortable bedroom.")
    garden = Room("Garden", "You step out into a beautiful garden.")

    # Connect rooms
    living_room.add_exit("north", kitchen)
    kitchen.add_exit("south", living_room)
    kitchen.add_exit("east", garden)
    garden.add_exit("west", kitchen)
    living_room.add_exit("east", bedroom)
    bedroom.add_exit("west", living_room)

    # Add items to rooms
    living_room.add_item(Item("Key", "A shiny key"))
    kitchen.add_item(Item("Knife", "A sharp kitchen knife"))
    garden.add_item(Item("Flower", "A colorful flower"))
    bedroom.add_item(Item("Book", "An old book"))

    # Create player and place in starting room
    player = Player(living_room)

    # Game loop
    while True:
        print("\n=== Current Location:", player.current_room.name, "===")
        print(player.current_room.description)
        
        command = input(">>> ").strip().lower()

        if command == "quit":
            print("Goodbye!")
            break
        elif command.startswith("go "):
            direction = command.split()[1]
            player.move(direction)
        elif command.startswith("take "):
            item_name = command.split()[1]
            player.take_item(item_name)
        elif command == "inventory":
            player.check_inventory()
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

