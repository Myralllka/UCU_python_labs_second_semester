class ZipReplace:
    """
    Class for working with folder with text files
    """
    def __init__(self):
        """
        initialization of the object of the class
        """
        self.search_string = input('string to search: ')
        self.replace_string = input('string to replace: ')

    def process_files(self, temp_directory):
        """
        Method for working with files in directory
        :param temp_directory: current directory
        """
        for filename in temp_directory.iterdir():
            with filename.open() as file:
                contents = file.read()
            contents = contents.replace(self.search_string,
                                        self.replace_string)
            with filename.open("w") as file:
                file.write(contents)
