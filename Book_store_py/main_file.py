from addbook import add_book
import sqlite3
print("[1] to search book in database")
print("\n[2] to add book to database")
i=int(input("\n"))
pri=0
choice='Y'
if i==1:
    while (choice=='y' or choice=='Y'):
        n=input("\nEnter name of book: ")
        book=sqlite3.connect('books_detail.db')
        try:
            cursor=book.cursor()
            cursor.execute("SELECT * FROM booktable WHERE name=?",(n,))
            result=cursor.fetchall()
            record=result[0]
            for j in range(0,len(record)):
                print(record[j], end='   |   ')
        
        except:
            print("\nNo book found.")
            break
        no=int(input("\nEnter number of copies: "))
        pri=pri+record[3]*no
        choice=input("\nAdd more books? Y/N ")
    print("\nTotal cost: ",pri )
    book.close()
    
elif i==2:
    add_book()

else:
    print("\nInvalid Input")
