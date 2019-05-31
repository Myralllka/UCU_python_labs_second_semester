from urllib.request import urlopen
import time


class WebPage:
    def __init__(self, url, regulation=86400):
        self.url = url
        self._content = None
        self._regulation = regulation
        self._uptime = 0

    @property
    def content(self):
        if time.time() - self._uptime >= self._regulation:
            print("Retrieving New Page...")
            self._content = urlopen(self.url).read()
            self._uptime = time.time()
        return self._content
