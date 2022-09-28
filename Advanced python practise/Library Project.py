class Library:
    def __init__(self, listofbooks):
        self.books = listofbooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print("*" + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days\n")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until book is returned\n")
            return False
    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for adding/returning this book! Hope you enjoyed reading it.\n")

class Student:
    def requestBook(self):
        self.book = input("Enter the name of book you want to borrow: \n")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of book you want to return: \n")
        return self.book

if __name__=="__main__":
    centraLibrary = Library(["Algorithms", "Django", "Clrs", "Python Notes"])
    student = Student()
    # centraLibrary.displayAvailableBooks() 
    while(True):
        welcomeMsg = '''====Welcome to central Library====
        Please Choose an option:
        1. Listing all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: \n"))
        if a == 1:
            centraLibrary.displayAvailableBooks()
        elif a==2:
            centraLibrary.borrowBook(student.requestBook()) 
        elif a==3:
            centraLibrary.returnBook(student.returnBook())
        elif a==4:
            print("Thanks for using this library! have a great day ahead\n")
            exit()
        else:
            print("Select correct option\n")
        