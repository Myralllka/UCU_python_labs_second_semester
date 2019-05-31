class Book:
    """
    class for representing books
    """

    def __init__(self, title: str, author: str, pages: int):
        """
        initialization of the object of book class
        :param title: book`s title
        :param author: book`s author
        :param pages: number of pages in the book
        current page - current page in the book
        bookmark_page - page that you want to remember
        """
        self.author = author
        self.pages = pages
        self.title = title
        self.current_page = 1
        self.bookmark_page = None

    def __str__(self):
        """
        method for representing the book in normal string
        :return: string with all needed info
        """
        tmp = 'page' if self.pages == 1 else 'pages'
        res = 'Book<{} by {}: {} {}, currently on page {}>' \
            .format(self.title, self.author, self.pages, tmp,
                    self.current_page)
        if self.bookmark_page is None:
            return res
        else:
            return res[:-1] + ', page {} bookmarked'.format(
                    self.bookmark_page) + '>'

    def __eq__(self, other) -> bool:
        """
        class for check are two books equal or not
        :param other: Book instance
        :return: if two instances are equal or not (True/False)
        """
        return (self.title == other.title and
                self.author == other.author and
                self.current_page == other.current_page and
                self.pages == other.pages and
                self.bookmark_page == other.bookmark_page)

    def turnPage(self, page: int):
        """
        Method for turning pages
        :param page: number of pages to turn forward or back
        """
        if 0 < self.current_page + page <= self.pages:
            self.current_page += page
        elif self.current_page + page <= 0:
            self.current_page = 1
        else:
            self.current_page = self.pages

    def getCurrentPage(self) -> int:
        """
        method for returning current page
        """
        return self.current_page

    def getBookmarkedPage(self):
        """
        method for returning current page
        :return: None if there is not bookmarks, number of bookmarked page
        if it exist
        """
        return self.bookmark_page

    def placeBookmark(self):
        """
        method for bookmarking the page
        """
        self.bookmark_page = self.current_page

    def turnToBookmark(self):
        """
        method to change the current page on bookmarked one if it exist
        """
        if not self.bookmark_page is None:
            self.current_page = self.bookmark_page

    def removeBookmark(self):
        """
        method for removing bookmark
        """
        self.bookmark_page = None
