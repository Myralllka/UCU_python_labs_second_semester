class TextMachine:
    """
    class for representing text machine
    """
    def __init__(self, text_count1, text_count2):
        """
        init of class instance
        """
        self.short_text = text_count1
        self.long_text = text_count2
        self.stext = text_count1
        self.ltext = text_count2

    def __str__(self):
        return "Text Machine:<{} texts; ₴{:2.2f} each>; <{} texts; ₴{:2.2f} " \
               "each>" \
            .format(self.short_text[0], self.short_text[1]/100,
                    self.long_text[0], self.long_text[1]/100)

    def __eq__(self, other):
        try:
            return self.stext == other.stext and self.ltext == other.ltext
        except:
            return 'something get wrong!'

    def __hash__(self):
        return hash(tuple([self.stext, self.ltext]))

    def is_empty(self):
        """
        check is empty machine or not
        """
        return not (self.short_text and self.long_text)

    def get_text_count(self):
        """
        :return: number of texts
        """
        return tuple([self.short_text[0], self.long_text[0]])

    def still_owe(self):
        return tuple([self.short_text[1], self.long_text[1]])

    def insert_money(self, tup):
        money, kind_of_text = tup
        if kind_of_text == 'short':
            # if self.stext[]
            self.short_text = tuple([self.short_text[0],
                                     self.short_text[1] - money])
            if self.short_text[1] > 0:
                res = tuple(["Still owe ₴{}".format(
                        round(self.short_text[1] / 100, 2)),
                    self.stext[1] - self.short_text[1]])
                res
            else:
                res = tuple(["Got a text!", self.long_text[1] - money])
                self.short_text = tuple([self.short_text[0] - 1,
                                         self.short_text[1]])
                self.stext = tuple([self.stext[0] - 1,
                                    self.stext[1]])
                return res
        elif kind_of_text == 'long':
            self.long_text = tuple([self.long_text[0],
                                    self.long_text[1] - money])
            if self.long_text >= 0:
                return tuple(["Still owe ₴{}".format(round(self.long_text[1] /
                                                           100, 2)),
                              self.ltext[1] - self.long_text[1]])
            else:
                res = (["Got a text!", self.long_text[1] - money])
                self.ltext = tuple([self.ltext[0] - 1,
                                    self.ltext[1]])
                return res

    def stock_machine(self, tup):
        self.stext = tuple([tup[0], self.stext[0]])
        self.ltext = tuple([tup[1], self.ltext[1]])
