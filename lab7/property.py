class Property:
    def __init__(self, square = '', beds = '', bathes = '', **kwargs ):
        super().__init__(**kwargs)
        self.square = square
        self.num_beds = beds
        self.num_bathes = bathes

    def display(self):
        print("Property info")
        print("property square: {}".format(self.square))
        print("property beds: {}".format(self.num_beds))
        print("property bathes: {}".format(self.num_bathes))

    def promt_init():
        return dict(square = input("Enter the square: "),
                    beds = input("Enter the number of bedrooms: "),
                    bathes = input("Enter the number of bathes:"))

    promt_init = staticmethod(promt_init)

class Apartment(Property):
    valid_laundries = ("none", "in_flat", "in_building")
    valid_balconies = ("no", "yes", "lodgy")

    def __init__(self, balcony = '', laundry = '', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print("Apartment info")
        print("laundries: {}".format(self.laundry))
        print("balconies: {}".format(self.balcony))

    def promt_init():
        parent_init = Property.promt_init()
        laundry = get_valid_input("What about laundry?",
                                  Apartment.valid_laundries)
        balcony = get_valid_input("What about balcony?",
                                  Apartment.valid_balconies)
        parent_init.update({"laundry" : laundry,
                            "balcony" : balcony})
        return parent_init

    prompt_init = staticmethod(promt_init)



def get_valid_input(input_string, valid_options):
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response








