from PIL import Image


class ScaleZip:
    """
    class for working with images
    """
    @staticmethod
    def process_files(temp_directory):
        """
        Method for working with files in directory
        :param temp_directory: current directory
        """
        x, y = list(
                map(int, input('Write here needed resolution, one of'
                               '(640*480), '
                               '(640*360), '
                               '(480*360), '
                               '(480*270), '
                               '(360*270), '
                               '(360*203):')
                    .strip().split('*')))
        x, y = 640, 480
        for filename in temp_directory.iterdir():
            im = Image.open(str(filename))
            scaled = im.resize((x, y))
            scaled.save(filename)
