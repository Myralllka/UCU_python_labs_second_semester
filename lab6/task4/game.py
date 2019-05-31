class Room:
    """
    class for representing rooms
    """

    def __init__(self, kind_of_room,
                 description=None,
                 item=None,
                 character=None):
        """
        Initialization of Room instance

        :param kind_of_room: str - kind of represented room (kitchen,
        ballroom etc)
        :param description: str - room description
        :param item: Item instance - Item that is in this room
        :param character: Enemy instance - Enemy that is in this room
        """
        self.description = description
        self.kind_of_room = kind_of_room
        self.item = item
        self.character = character
        self.linked_rooms = {}

    def __str__(self):
        """
        Print class information for NONProgrammers

        :return: str - message for users that contain room name - kind of room
        """
        return '{}'.format(self.kind_of_room)

    def __repr__(self):
        """
        Print class information for Programmers (in interactive mode)

        :return: str - message for users that contain room name - kind of room
        """
        return '{}'.format(self)

    def set_description(self, description):
        """
        Initialize Room instance description

        :param description: str - description of the room
        """
        self.description = description

    def set_character(self, character):
        """
        Initialize Room instance character

        :param character: Enemy instance - Enemy situated in this room
        """
        self.character = character

    def set_item(self, item):
        """
        Initialize Item instance in the room

        :param item: Item instance - Item situated in this room
        """
        self.item = item

    def link_room(self, other, direction):
        """
        Link Room instances with other rooms by cardinal directions to move
        around them

        :param other: Rome instance other room to link with
        :param direction: str - one of four cardinal directions: north, east,
        south, west
        """
        possible = ['north', 'east', 'south', 'west']
        if direction in possible:
            self.linked_rooms[direction] = other
        else:
            print("Unavailable direction")

    def move(self, direction: str):
        """
        Method to change room

        :param direction: str - one of four cardinal directions: north,east,
        south, west
        :return: Room instance - other room
        """
        return self.linked_rooms[direction]

    def get_details(self):
        """
        Method to print details about the room - kind of the room and its
        description and rooms near this room
        """
        print('{}\n'.format(self.kind_of_room) + '-' * 20 + '\n{}'.format(
                self.description))
        for each in self.linked_rooms:
            print('The {} is {}'.format(self.linked_rooms[each], each))

    def get_character(self):
        """
        Method to return characters situated in the room

        :return: Enemy instance
        """
        return self.character

    def get_item(self):
        """
        Method to return items situated in the room

        :return: Item instance
        """
        return self.item


class Enemy:
    """
    class for representing enemies
    """
    defeated = 0

    def __init__(self,
                 name,
                 description='',
                 phrase='',
                 weakness=None):
        """
        Initialization of Enemy class
        :param name: str - character name
        :param description: str - character description
        :param phrase: str - phrase for character to talk with player
        :param weakness: Item instance - Item for which enemy is weak
        """
        self.name = name
        self.description = description
        self.phrase = phrase
        self.weakness = weakness

    def __str__(self):
        """
        Print class information for NONProgrammers

        :return: str - message for users that contain enemy description
        """
        return self.description

    def set_conversation(self, phrase):
        """
        Initialization of enemy`s phrase
        :param phrase: str - phrase for character to talk with player
        """
        self.phrase = phrase

    def set_weakness(self, weakness):
        """
        Initialisation of enemy`s weakness item

        :param weakness: Item instance - Item for which enemy is weak
        """
        self.weakness = weakness

    def describe(self):
        """
        Method to print enemy`s name and description
        """
        print('{} is here!'.format(self.name))
        print(self.description)

    def talk(self):
        """
        Method to print enemy`s phrase
        """
        print('[{} says]: {}'.format(self.name, self.phrase))

    def fight(self, weakness):
        """
        Method to fight with enemy

        :param weakness: Item instance - Item for which enemy is weak
        :return: True if enemy is weak for this weakness, False if not
        """
        if self.weakness == weakness:
            print("You fend {} off with the {}".format(self.name, weakness))
            Enemy.defeated += 1
            return True
        return False

    @staticmethod
    def get_defeated():
        """
        Method for checking number of defeated enemies
        :return: int - self.defeated, number of defeated enemies
        """
        return Enemy.defeated


class Item:
    """
    Class for representing Items
    """
    def __init__(self, name, description=''):
        """
        Initialization of Item instances

        :param name: str - Item name
        :param description: str - Item description
        """
        self.name = name
        self.description = description

    def __str__(self):
        """
        Print class information for NONProgrammers

        :return: str - message for users that contain item name
        """
        return '{}'.format(self.name)

    def set_description(self, description):
        """
        Initialize Item instance description

        :param description: str - description of the item
        """
        self.description = description

    def describe(self):
        """
        Method to print item`s name and description
        :return:
        """
        print('The [{}] is here - {}'.format(self.name, self.description))

    def get_name(self):
        """
        Method to get item name
        :return: str - self.name
        """
        return self.name
