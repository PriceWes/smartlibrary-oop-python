from book import Book

class Magazine(Book):
    def __init__(self, title, editor, year):
        #We still call the parent constructor but use editor instead of author
        super().__init__(title, editor, year)

    def borrow(self):
        """
        Override borrow method == Magazine can't be borrowed
        """
        return f"{self.title} is a magazine and can not be borrowed"