class errors(Exception):
    pass


class BaseError():
    FILENOTFOUND = errors("file not found")

raise BaseError.FILENOTFOUND