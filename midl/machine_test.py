from machine import TextMachine


def testTextMachineClass():
    print("Testing Text Machine class...", end="")
    # Text machines have four main properties:
    # how many text of two type they contain and the price of each type text.
    # A new text machine starts with two texts type.
    tm1 = TextMachine((75, 125), (25, 245))
    assert (str(tm1) == "Text Machine:<75 texts; ₴1.25 each>; "
                        "<25 texts; ₴2.45 each>""")
    assert (tm1.is_empty() == False)
    assert (tm1.get_text_count() == (75, 25))
    assert (tm1.still_owe() == (125, 245))
    s = set()
    s.add(tm1)
    # When the user inserts money and text type, the machine returns a message
    # about their status and any change they need as a tuple.
    tm1.insert_money((20, 'short'))
    # assert (tm1.insert_money((20, 'short')) == ("Still owe ₴1.05", 20))
    assert (tm1.still_owe() == (105, 245))
    assert (tm1.get_text_count() == (75, 25))
    tm1.insert_money((5, 'short'))

    # When the user has paid enough money, they get a text and
    # the money owed resets.
    print(tm1.insert_money((100, 'short')))
    assert (tm1.insert_money((100, 'short')) == ("Got a text!", 125))
    assert (tm1.get_text_count() == (74, 25))
    assert (tm1.still_owe() == (125, 245))
    assert (str(tm1) == "Text Machine:<74 texts; ₴1.25 each>; "
                        "<25 texts; ₴2.45 each>")

    # If the user pays too much money, they get their change back with the
    # text.
    assert (tm1.insert_money((500, 'long')) == ("Got a text!", 255))
    assert (tm1.get_text_count() == (74, 24))
    assert (tm1.still_owe() == (125, 245))
    assert (str(tm1) == "Text Machine:<74 texts; ₴1.25 each>; "
                        "<24 texts; ₴2.45 each>")

    # Machines can become empty
    tm2 = TextMachine((1, 120), (0, 245))
    assert (str(tm2) == "Text Machine:<1 texts; ₴1.20 each>")
    assert (tm2.is_empty() == False)
    assert (tm2.insert_money((120, "short")) == ("Got a text!", 120))
    assert (tm2.get_text_count() == (0, 0))
    assert (tm2.is_empty() == True)
    assert (str(tm2) == "Text Machine:<0 texts; ₴1.20 each>")

    # Once a machine is empty, it should not accept money until it is restocked.
    assert (tm2.insert_money((25, "short")) == ("Machine is empty", 25))
    assert (tm2.insert_money((120, "short")) == ("Machine is empty", 120))
    assert (tm2.still_owe() == (120, 245))
    tm2.stock_machine((20, 20))  # Does not return anything
    assert (tm2.get_text_count() == (20, 20))
    assert (tm2.is_empty() == False)
    assert (str(tm2) == "Text Machine:<20 texts; ₴1.20 each>; "
                        "<20 texts; ₴2.45 each>")
    assert (tm2.insert_money((25, "short")) == ("Still owe ₴0.95", 25))
    assert (tm2.still_owe() == (95, 245))
    tm2.stock_machine((20, 0))
    assert (tm2.get_text_count() == (40, 20))

    # We should be able to test machines for basic functionality
    tm3 = TextMachine((25, 100), (25, 200))
    tm4 = TextMachine((25, 100), (25, 200))
    tm5 = TextMachine((20, 100), (15, 200))
    tm6 = TextMachine((25, 120), (25, 245))
    tm7 = "Text Machine"
    assert (tm3 == tm4)
    assert (tm3 != tm5)
    assert (tm3 != tm6)
    assert (tm3 != tm7)  # should not crash!

    assert (tm3 not in s)
    s.add(tm4)
    assert (tm3 in s)
    s.remove(tm4)
    assert (tm3 not in s)
    assert (tm4.insert_money((50, "short")) == ("Still owe ₴0.50", 50))
    assert (tm3 != tm4)
    print("Done!")


testTextMachineClass()
