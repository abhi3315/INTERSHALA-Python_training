import sqlite3

def add_book():
    Books=sqlite3.connect('books_detail.db')   
    num= int(input("Enter ID of book: "))
    bookname=input("Enter name: ")
    author=input("Enter Author name: ")
    price=float(input("Enter price: "))
        
    #try block to catch exceptions
    try:
        cursbook=Books.cursor()
        cursbook.execute("INSERT INTO booktable (ID, name, author, price) VALUES (?,?,?,?);", (num, bookname, author, price))
        Books.commit()
        print ("One record added successfully.")

    #except block to handle exceptions    
    except:
        print ("Book couldn`t be added to database")
        Books.rollback()
        
    Books.close()

if __name__=="__main__":
    add_book()
