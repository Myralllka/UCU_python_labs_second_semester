class Bird:
    """
    class for representing birds
    """

    def __init__(self, name: str):
        """
        initialization of bird instance object
        :param name: bird`s name
        eggs - number of bird`s eggs
        """
        self.name = name
        self.eggs = 0

    def __repr__(self):
        """
        method for representing bird object
        :return: needed string
        """
        tmp = 'egg' if self.eggs == 1 else 'eggs'
        return '{} has {} '.format(self.name, self.eggs) + tmp

    def countEggs(self) -> int:
        """
        method for counting bird`s eggs
        :return: number of eggs
        """
        return self.eggs

    def fly(self) -> str:
        """
        return bird`s phrase
        :return: needed string
        """
        return 'I can fly!'

    def layEgg(self):
        """
        function to increment eg`s number
        """
        self.eggs += 1


class Penguin(Bird):
    """
    class for representing penguin
    """
    def fly(self) -> str:
        """
        return bird`s phrase
        :return: needed string
        """
        return 'No flying for me.'

    def swim(self) -> str:
        """
        return bird`s phrase
        :return: needed string
        """
        return 'I can swim!'


class MessengerBird(Bird):
    """
    class for representing message bird
    """
    def __init__(self, name: str, message=''):
        """
        initialization of classes object
        :param name: bird`s name
        :param message: bird`s message
        """
        super().__init__(name)
        self.message = message

    def deliverMessage(self) -> str:
        """
        return bird`s phrase
        :return: needed string
        """
        return self.message
