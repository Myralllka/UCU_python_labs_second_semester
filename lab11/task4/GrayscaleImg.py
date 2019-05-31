from arrays import *


class GrayscaleImg:
    """
    class for representing Grayscale images
    """
    def __init__(self, rows, cols):
        self._items = Array2D(cols, rows)
        self.set_up()

    def __str__(self):
        res = ''
        for i in range(self.height()):
            for j in range(self.width()):
                res += str(self._items[i, j]).zfill(3)
            res += '\n'
        return res[:-1]

    def __getitem__(self, item):
        row = item[0]
        col = item[1]
        return self._items[row, col]

    def __setitem__(self, key, value):
        row = key[0]
        col = key[1]
        self._items[row, col] = value

    def width(self):
        """
        :return: image width
        """
        return self._items.num_cols()

    def height(self):
        """
        :return: image height
        """
        return self._items.num_rows()

    def clear(self, value):
        """
        method for clearing image
        :param value: value that will be after the clearing
        """
        self.set_up(value)

    def set_up(self, symbol=0):
        """
        initialisation the image with 0 symbols
        """
        self._items.clear_array(symbol)
