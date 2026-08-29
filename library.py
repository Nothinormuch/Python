def addBook(Library,title,author,year):#Stucture of library is [(BookTitle, BookAuthor, BookYear,etc),(...),(...)]
    Library.append((title,author,year))
    print(f"Book : {title} by {author} added to the library!")
    print(Library)
    return True
def addBookInput(Library):
    title=input("Enter the title of the book: ")
    author=input("Enter the name of the author of the book: ")
    year=input("Enter the year year of publication of the book: ")
    return Library,title,author,year


def deleteBook(Library,title,author):
    for i in range(len(Library)):
        if Library[i][0]==title and Library[i][1]==author:
            Library.pop(i)
            print(f"Book : {title} by {author} removed from the library!")
            return True
    print(f"There is no book with the title {title} and the author {author} in the Library!")
def deleteBookInput(Library):
    title=input("Enter the title of the book: ")
    author=input("Enter the name of the author of the book: ")
    return Library,title,author



def searchBook(Library,title):
    for i in range(len(Library)):
        if Library[i][0]==title:
            print(f"Book : {title} by {Library[i][1]} was found in the library!\n\nThe Library Entry: \n{Library[i]}")
            return True
    print(f"There is no book with the title {title} and the author {Library[i][1]} in the Library!")
def searchBookInput(Library):
    title=input("Enter the title of the book: ")
    return Library,title



def pushAll(Library,State):
    print("Listing the {} books in the Library!".format(len(Library)))
    for i in range(len(Library)):
        print(f"Book {i+1}:\n\t\tTitle: {Library[i][0]}\n\t\tAuthor: {Library[i][1]}\n\t\tYear: {Library[i][2]}\n\n")
def pushAllInput(Library):
    return Library,True