class Street:
    """
    Class for representation Street instance
    """

    def __init__(self, name: str, description: str):
        """
        Initialization of Street class
        :param name: street name
        :param description: street description
        linked_streets - dict - dictionary for linked streets, where keys
        are directions and values - linked streets
        items - list of Item instances on this street
        characters - list of Character instances on this street
        """
        self.name = name
        self.description = description
        self.linked_streets = {}
        self.items = []
        self.characters = []
        self.buildings = {}

    def __str__(self):
        """
        print information for user interface with "print" function
        :return:str - needed information
        """
        return '{}'.format(self.name)

    def __repr__(self):
        """
        print information for interactive interface
        :return:str - needed information
        """
        return '{}'.format(self.name)

    def add_item(self, item: object):
        """
        added an Item instance on the street
        :param item: any Item instance
        """
        self.items.append(item)

    def add_character(self, character: object):
        """
        added any Character on the street
        :param character: any Character instance
        """
        self.characters.append(character)

    def link_street(self, other: object, direction:str):
        """
        link two streets to each other
        :param other: Street instance - any street
        :param direction: one of main directions
        """
        self.linked_streets[direction] = other

    def ch_street(self, direction:str):
        """
        to move around the city by links
        :param direction: any direction to move
        :return: Street instance
        """
        return self.linked_streets[direction]

    def get_details(self):
        """
        print information about the street and the linked streets
        """
        print('{}\n'.format(self.name) + '-' * 20 + '\n{}'.format(
                self.description))
        for each in self.linked_streets:
            print('{} знаходиться [{}]'.format(self.linked_streets[each],
                                               each))

    def get_items(self):
        """
        get all items from Street items
        :return: list of street Items
        """
        return self.items

    def get_characters(self):
        """
        get all Characters from the Street characters
        :return: list of street Characters
        """
        return self.characters
