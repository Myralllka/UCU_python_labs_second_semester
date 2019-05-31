class Character:
    """
    Class for representing Character for the game
    """
    # main character health
    hero_health = 10
    # flag to check if you save needed character or not
    saved = False

    def __init__(self, name, status, description, weakness, health, phrase):
        """
        initialization of class
        :param name: str - character`s name
        :param status:str - enemy or friend, status of the character
        :param description: str - description of enemy, that contained hint about how to kill that enemy
        :param weakness: Item instance - Item that can kill/change character
        :param health: int - health of the character
        :param phrase:str - phrase that contained important (or just interesting) information about character
        """
        self.name = name
        self.status = status
        self.description = description
        self.weakness = weakness
        self.health = health
        self.phrase = phrase
        self.power = 1

    def describe(self):
        """
        print Character instance description and all needed information
        """
        print('{} - {} (здоров\'я: {}, статус: {})'.format(self.name,
                                                           self.description,
                                                           self.health,
                                                           self.status))

    def talk(self):
        """
        print Character phrase
        """
        print('[{}]: {}'.format(self.name, self.phrase))

    def fight(self, item):
        """
        function to fight with character
        :param item: Item instance - item that main character fight with
        :return: 'miss' if Item is not character weakness, 'hurt' if it is
        """
        if item != self.weakness:
            return 'miss'
        return 'hurt'

    def __eq__(self, other):
        """
        Check instances for equal
        :param other: Character instance
        :return: True if Characters names are equal
        """
        return self.name == other.name
