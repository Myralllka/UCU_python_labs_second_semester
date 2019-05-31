import shutil
import zipfile
from pathlib import Path


class ZipProcessor:
    """
    class for representing work with archives
    """
    def __init__(self, zipname, obj):
        """
        initialization of the object of the class
        :param zipname: name of the processing file
        :param obj: object to process it
        """
        self.zipname = zipname
        self.obj = obj
        self.temp_directory = Path('unzipped_{}'.format(zipname[:-4]))
        self.process_zip()

    def process_zip(self):
        """
        Method for extracting, processing and compressing the archive
        """
        self.unzip_files()
        self.process_files()
        self.zip_files()

    def process_files(self):
        """
        Method for processing archive
        """
        self.obj.process_files(self.temp_directory)

    def unzip_files(self):
        """
        Method for extracting the archive
        """
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.zipname) as zp:
            zp.extractall(str(self.temp_directory))

    def zip_files(self):
        """
        Method for compressing the archive
        """
        with zipfile.ZipFile(self.zipname, 'w') as file:
            for filename in self.temp_directory.iterdir():
                file.write(filename, filename.name)
        shutil.rmtree(self.temp_directory)
