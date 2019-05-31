class Flower:
    def __init__(self, colour, num, price):
        if not (isinstance(colour, str) and
                isinstance(num, int) and
                isinstance(price, int)):
            raise TypeError
        self.num = num
        self.colour = colour
        self.price = price


class Rose(Flower):
    def __init__(self, colour, num, price):
        super().__init__(colour, num, price)


class Tulip(Flower):
    def __init__(self, colour, num, price):
        super().__init__(colour, num, price)


class Chamomile(Flower):
    def __init__(self, colour, num, price):
        super().__init__(colour, num, price)


class FlowerSet:
    def __init__(self, flowers):
        if flowers == []:
            raise TypeError
        self.flowers = flowers


class Bucket:
    def __init__(self, flowersets):
        if flowersets == []:
            raise TypeError
        self.flowersets = flowersets

    def price_all(self):
        res = 0
        for fset in self.flowersets:
            for flower in fset.flowers:
                res += flower.price
        return res
