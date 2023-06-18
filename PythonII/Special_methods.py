class Book:
    def __init__(self, title, author, pages) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        
    #Special method, string representation of object
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        pass
        
book = Book("Python", "Emmy", 200)
print(book)
print(len(book))