class LibraryItem:
    def __init__ (self,title,author,publication_year):
        self.title =title
        self.author = author
        self.publication_year = publication_year

    def __str__():
        return LibraryItem
    
class Book(LibraryItem):
    def __init__ (self,fields,isbn):
        self.fields=fields
        self.isbn =isbn
    def __str__():
        print( Book)
        
my_library_item = LibraryItem("littlewomen", "louisa may alcot", 1956)
my_book= Book( "romance", 1920293)
my_book.__str__()