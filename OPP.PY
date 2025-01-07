class Librarybook:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def borrow(self):
        print("you can borrow this book")

my_library_book = Librarybook("little women", "Louisa Alcott")


class Magazine(Librarybook):
    def __init__(self,daysSinceIssue):
        self.__daysSinceIssue= daysSinceIssue
    
    def borrow (self):
        if self.__daysSinceIssue>= 20:
            print("you can borrow this magazine")
        else:
            print("you can borrow this magazine")


my_Magazine =Magazine(31)
my_Magazine.borrow()