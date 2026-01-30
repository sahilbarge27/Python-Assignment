class BookStore:
    NoOfBooks = 0   # class variable

    def _init_(self, name, auther):
        self.name = name
        self.author = auther
        BookStore.NoOfBooks += 1

    def Display(self):
        print(self.name, "by", self.author, ". No of books:", BookStore.NoOfBooks)


# Example usage
obj1 = BookStore("Linux System Programming", "Robert Love")
obj1.Display()

obj2 = BookStore("C Programming", "Dennis Ritchie")
obj2.Display()