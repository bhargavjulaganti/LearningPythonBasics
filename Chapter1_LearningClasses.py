class Book():
    BOOK_TYPES = ('HardCover', 'E-book')

    # TODO: double-underscore properties are hidden from other classes
    __booklist = None

    # TODO: Create class method
    # This is at class level
    @classmethod
    def getBookTypes(cls):
        return cls.BOOK_TYPES

    # static methods do not receive class or instance arguments
    # and usually operate on data that is not instance- or
    # class-specific
    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    def __init__(self, title, author, price, bookType):
        self.title = title
        self.author = author
        self.price = price
        if (not bookType in Book.BOOK_TYPES):
            raise ValueError(f"{bookType} is not valid book type")
        else:
            self.bookType = bookType

    # TODO: Create instance methods
    def getPrice(self):
        if hasattr(self, '_discount'):
            return self.price - (self.price * self._discount)
        return self.price

    # Notes: In Java and C# we can create private variables, but not in python
    # Hence we name those with "_"
    # That means we should not use those variables outside of this class
    def setDiscount(self, amount):
        self._discount = amount


# TODO: Create book object

b1 = Book("Python Learning", "Bhargava", 100, "HardCover")
b2 = Book("C# Learning", "microsoft", 100, "E-book")

# print(b1.title)

# # Try setting discount
# print(b1.getPrice())
# b1.setDiscount(.15)
# print(b1.getPrice())

# Access Book types at class level
print(Book.getBookTypes())


# TODO: Use the static method to access a singleton object
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)




#### ****************************************************************
# Below code raises exceptions, added for learning purpose
#### ****************************************************************

#TODO: Create invalid book type

# b2 = Book("C# Learning", "microsoft", 100, "Learning") # should throw error