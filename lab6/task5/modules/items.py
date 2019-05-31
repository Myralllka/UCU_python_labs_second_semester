class Item:
    """
    Class for Item representation
    """
    def __init__(self, name, description, power):
        """
        initialization of Item class
        :param name: str - Item name
        :param description: str - item description
        :param power: int - Item power
        """
        self.name = name
        self.description = description
        self.power = power

    def __str__(self):
        """
        print information for user interface with "print" function
        :return:str - needed information
        """
        return '{} - {} ({})'.format(self.name,
                                     self.description,
                                     self.power)

    def __repr__(self):
        """
        print information for interactive interface
        :return:str - needed information
        """
        return '{}:{},{}'.format(self.name,
                                 self.description,
                                 self.power)

    def describe(self):
        """
        print Item`s description with important information
        """
        print('тут у нас [{}] - {} (сила: {})'.format(self.name,
                                                      self.description,
                                                      self.power))

    def __eq__(self, other):
        """
        Check instances for equal
        :param other: Item instance
        :return: True if Items names are equal, False otherwise
        """
        return self.name == other.name
