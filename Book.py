class Book():
    def __init__(self, title, isbn, author, year):
        self.title = title
        self.isbn = isbn
        self.author = author
        self.year = year

    def __str__(self):               #change to string
        _str = self.title + "\n" + str(self.isbn) + "\n\t" + self.author + "\n\t" + str(self.year) + "\n\n"
        return _str

    def __eq__(self, other):        #to compare if equal
        return (self.isbn == other.isbn)

    def __lt__(self, other):        #to compare if less than
        return (self.isbn < other.isbn)
