class Book:
    def __init__ (self, title, author, year):
        #self- stores all info in the book object
        # Constructor method to initializes the book object
        self.title = title
        self.author = author
        self.year = year
        self.available = True #sets availability to true by default
        self.__rating = 0

    def borrow(self):
        """
        Marks the book as borrowed if the book is available
        """
        if self.available:
            self.available = False
            return f"You have borrowed '{self.title}'."
        return f"'{self.title}' is currently unavailable."
    
    def return_book(self):
            """
            Marks the book as returned
            """
            self.available = True
            return f"'{self.title}' has ben returned"
    
    def get_details(self):
         """
         Returns formatted book info
         """
         return f"{self.title} by {self.author} {self.year}"
    
    def set_rating(self, rating):
         """
         Set Rating from 0 to 5 for the book
         This is an example of encapsulation: rating is private
         """
         if 0 <= rating <= 5:
            self.__rating = rating
         else:
              print("Rating must be between 0 and 5")
    
    def get_rating(self):
         """
         Get the current ratings of the book
         """
         return self.__rating
    
    #Book.get_details()
    #Book.available = 