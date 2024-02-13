class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")
        print("File has been created.")

    def __del__(self):
        self.file.close()
        print("Quitting")

    def listBook(self):
        list = self.readFiletoList()
        if len(list)==0:
            print("There is no book in the list.")
            return
        for i in range(0, len(list)):
            book = list[i].split(",")
            print(f"\nBook Name:{book[0]}\nBook Author:{book[1]}\n")

    def addBook(self):
        list = []
        seperator = ","
        list.append(input("Please input the book title:"))
        list.append(input("Please input the author:"))
        list.append(input("Please input the release year:"))
        list.append(input("Please input the number of pages:"))
        recentBook=seperator.join(list)
        list = self.readFiletoList()
        list.append(recentBook)
        self.writeFile(list)
    def readFiletoList(self):
        list = []
        with open('books.txt', 'r') as file:
            for line in file:
                list.append(line.strip())
        return list
    def writeFile(self,list):
        with open('books.txt', 'w') as file:
            for i in list:
                file.writelines(i+"\n")

    def removeBook(self):
        bookTitle = input("Please input the title to delete:")
        list = self.readFiletoList()
        for line in list:
            lineIterator = line.split(",")
            if(lineIterator[0]==bookTitle):
                list.remove(line)
                print("Successfully removed.")
        self.writeFile(list)

lib = Library()
while True:
    print("***MENU***\n1)List Books\n2)Add Book\n3)Remove Book\nq)Quit")
    userInp = input("Select your choice:")
    if userInp == "1":
        lib.listBook()
    elif userInp == "2":
        lib.addBook()
    elif userInp == "3":
        lib.removeBook()
    elif userInp == "q":
        del lib
        break
    else:
        print("Please type correctly.")






