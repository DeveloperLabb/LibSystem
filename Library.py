class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")
        print("File has been created.")

    def __del__(self):
        self.file.close()
        print("Object has been deleted.")

    def listBook(self):
        list = []
        with open('books.txt', 'r') as file:
            for line in file:
                list.append(line.strip())
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
        list = []
        with open('books.txt', 'r') as file:
            for line in file:
                list.append(line.strip())
        list.append(recentBook)
        with open('books.txt', 'w') as file:
            for i in list:
                file.writelines(i+"\n")


lib = Library()
#lib.listBook()
lib.addBook()


