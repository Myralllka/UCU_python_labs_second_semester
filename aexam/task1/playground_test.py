from playground import Carousel, Car, Playground
# a carousel has a type, capacity, price and size
c1 = Carousel("DE501", 3, 11000, length = 1400, wigth = 1400, higth = 700)
assert(str(c1) == "DE501 house 3: [length:1400, wigth:1400, higth:700]")
# a carousel needs a place to put (area+50%)
assert(c1.place_area() == 2.94)
# a car has a type, price and size
c2 = Car("DE401", 30000, length = 2500, wigth = 1080, higth = 2000)
assert(str(c2) == "DE401: [length:2500, wigth:1080, higth:2000]")
# a car needs a place to put (area+100%)
assert(c2.place_area() == 5.4)
# a playground has a name and size
p1 = Playground("DE", length = 3, wigth = 5)
assert(str(p1) == "DE: []")
# a carousel and car can be added
assert(p1.add_thing(c1) == True)
assert(p1.add_thing(c2) == True)
# can't to add things if there is no place to put them
c3 = Car("DE401", 30000, length = 2500, wigth = 1080, higth = 2000)
c4 = Carousel("DE501", 3, 11000, length = 1400, wigth = 1400, higth = 700)
assert(p1.add_thing(c4) == True)
assert(p1.add_thing(c3) == False)
assert(str(p1) == "DE: ['DE501', 'DE401', 'DE501']")
# can remove the most recent thing
assert(p1.remove_thing() == True)
assert(str(p1) == "DE: ['DE501', 'DE401']")
# can't remove a thing from an empty carousel
assert(Playground("PE", length = 3, wigth = 5).remove_thing() == False)
# can calculate the total price of Playground
assert(p1.price() == 41000)
assert(c4 != c1)
assert(c1 != "DE501") # should not crash!


"""

assert(c1.remove_child(mom_call = 'Os') == False)
assert(str(c1) == "DE501 house 3: ['Orislava']")
assert(c1.add_child("Oksana") == True) # that frees up space!
c2 = Carousel("DE505", 4)
# can't remove a child from an empty carousel
assert(c2.remove_child() == False)

assert(c2 == Carousel("DE505", 4))
assert(c2 != c1)
assert(c2 != "DE505") # should not crash!

# an Attraction is a Carousel with a name and a capacity
# an Attraction has a supervisor of the attraction
a1 = Attraction("Children Train", 10, 'Den')
assert(str(a1) == "Children Train house 10: ['Den']")
assert(a1.add_child("Denny") == True)
assert(str(a1) == "Children Train house 10: ['Den', 'Denny']")
# an attraction knows whether it's currently being run
a1.start_attraction()
# while it's being runned, you can't remove children
assert(a1.remove_child() == False)
a1.stop_attraction()
# when the attraction is stopped, normal rules apply
assert(a1.remove_child() == True)
assert(a1.remove_child() == False)
"""