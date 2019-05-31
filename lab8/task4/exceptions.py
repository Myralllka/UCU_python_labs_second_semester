class DocumentException(Exception):
    def __init__(self, message=''):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class OutOfDocument(DocumentException):
    pass


class EmptyFilename(DocumentException):
    def __init__(self):
        super().__init__(message='Pleas, input any filename!')


class TooMuchCharacters(DocumentException):
    pass
