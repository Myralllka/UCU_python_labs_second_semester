class Channel:
    def __init__(self, name, frequency, playlist):
        self.frequency = frequency
        self.playlist = playlist
        self.name = name


    def getFrequency(self):
        return self.frequency

    def __str__(self):

        return "Channel {} on {}, playlist: {}".format(self.name,
                                                   self.frequency,
                                                  self.playlist)

    def __eq__(self, other):
        try:
            return self.frequency == other.frequency
        except AttributeError:
            return self.frequency == other

    def __hash__(self):
        return hash(self.name)


class Radio:
    def __init__(self, channels, freq):
        self.channels = channels
        self.freq = freq

    def getCurrentFrequency(self):
        return self.freq

    def getCurrentChannel(self):
        for channel in self.channels:
            if round(channel, 1) == round(self.freq, 1):
                return float(round(self.freq, 1))
