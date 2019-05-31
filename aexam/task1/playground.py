class Machine:
    def __str__(self):
        return '{} house {}: [length:{}, wigth:{}, higth:{}]'.format(
                self.typee, self.capacity, self.length, self.wight, self.higth
                )

    def place_area(self):
        """
        a carousel needs a place to put (area+50%)
        :return: area for carousel
        """
        area = self.wight * self.length / 1000000
        area += area * self.mul
        return round(area, 2)


class Carousel(Machine):
    def __init__(self, typee, capacity, price, length, wigth, higth):
        """
        initialization of class instance
        a carousel has a type, capacity, price and size
        """
        self.typee = typee
        self.capacity = capacity
        self.price = price
        self.length = length
        self.wight = wigth
        self.higth = higth
        self.mul = .5


class Car(Carousel):
    def __init__(self, typee, price, length, wigth, higth):
        """
        initialization of Car instance
        """
        self.typee = typee
        self.price = price
        self.length = length
        self.wight = wigth
        self.higth = higth
        self.mul = 1

    def __str__(self):
        return '{}: [length:{}, wigth:{}, higth:{}]'.format(
                self.typee, self.length, self.wight, self.higth
                )


class Playground:
    def __init__(self, name, length, wigth):
        """
        initialization of playground instance
        """
        self.typee = name
        self.length = length
        self.wigth = wigth
        self.playground = []
        self.free_area = length * wigth

    def __str__(self):
        if self.playground:
            return '{}: [\'{}\']'.format(self.typee, "', '".join([i.typee for
                                                                  i in
                                                                  self.playground]))
        return '{}: []'.format(self.typee)

    def add_thing(self, element):
        """
        a carousel and car can be added
        can't to add things if there is no place to put them
        """
        if self.free_area - element.place_area() >= 0:
            self.playground.append(element)
            self.free_area -= element.place_area()
            return True
        else:
            return False

    def remove_thing(self):
        """
        can remove the most recent thing
        can't remove a thing from an empty carousel
        """
        if self.playground:
            self.free_area += self.playground[-1].place_area()
            self.playground.pop()
            return True
        return False

    def price(self):
        """
        can calculate the total price of Playground
        """
        pr = 0
        for each in self.playground:
            pr += each.price
        return pr
