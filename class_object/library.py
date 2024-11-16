
from class_object.books import Book
class Library:
    def __init__(self):
        self.books=[]
    
    def add_book(self,book):
        self.books.append(book)
        return f"{book.title} has been added in Library."
    
    def list_book(self):
        return f"Book List : {[book.title for book in self.books]}"
    
    def find_book(self,title):
        for book in self.books:
            if book.title==title:
                return f"Book Found : {book.title}" 
        return None

# creating new book
book1=Book("Ramayana","sage Valmik",1242)
book2=Book("Arthashastra","Chanakya",7654)
book3=Book("Charaka Samhita","Harshavardhana",76543456)

# adding books in Library.

my_library=Library()
print(my_library.add_book(book1))
print(my_library.add_book(book2))
print(my_library.add_book(book3))

print(my_library.list_book())
print(my_library.find_book("Ramayana"))

print(f"Issue Book : {book1.check_in()}")
print(f"Issue Book : {book1.check_in()}")
print(f"Retunr Book : {book1.check_out()}")







    
    