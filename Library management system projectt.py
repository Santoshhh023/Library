#Connecting MYSQL database to python program as C
import mysql.connector as c
mydb =c.connect(host="localhost",user="root",password="",database="")

#Main program to take input from the user according to choice given  
def main():
    print("""--------------->>>>>>>>> LIBRARY MANAGEMENT SYSTEM <<<<<<<<<<<------------------
  
                             1.Add Book
                             2.Issue Book
                             3.Submit Book
                             4.Delete book
                             5.Display book
        """)
    choice = input("Enter your choice given above:")
    print("________________________________________________________________________________")
    if(choice == '1'):
        Add_Book()
    elif(choice == '2'):
        Issue_Book()
    elif(choice == '3'):
        Submit_Book()
    elif(choice == '4'):
        Delete_Book()
    elif(choice == '5'):
        Display_Books()
    else:
        print("Incorrect choice !!")
    main()
    
#To Add Books in Books Table in database
def Add_Book():
    BOOK_NAME = input("Enter Book name: ")
    BOOK_CODE = input("Enter Book Code: ")
    QUANTITY = input("Total Books: ")
    TITLE_OR_SUBJECT = input("Enter Subject: ")
    data = (BOOK_NAME,BOOK_CODE,QUANTITY,TITLE_OR_SUBJECT)
    sql = "insert into BOOK values(%s,%s,%s,%s)"
    c = mydb.cursor()
    c.execute(sql,data)
    mydb.commit()
    print("________________________________________________________________________________")
    print("""BOOK ADDED TO LIBRARY SUCCESSFULLY !!
             THANK YOU VERY MUCH
             HAVE A NICE DAY:)""")
    main()

#To Issue Book by taking deatils from user and updating Books table
def Issue_Book():
    BOOK_NAME = input("Enter Your name: ")
    ENROLLMENT_NUMBER  = input("Enter Your Roll Number: ")
    BOOK_CODE = input("Enter Book code: ")
    DATE = input("Enter Date(YYYY/MM/DD): ")
    sql  = "insert into BOOK_ISSUE values(%s,%s,%s,%s)"
    data =(BOOK_NAME,ENROLLMENT_NUMBER,BOOK_CODE,DATE)
    c = mydb.cursor()
    c.execute(sql,data)
    mydb.commit()
    print("________________________________________________________________________________")
    print("BOOK ISSUED TO : ",name)
    Book_Update(code,-1)

#To Submit Book and updating Books table with the help of BooK Update function 
def Submit_Book():
    BOOK_NAME = input("Enter Your Name: ")
    ENROLLMENT_NUMBER  = input("Enter Your Enrollment Number: ")
    BOOK_CODE = input("Enter Book code: ")
    DATE = input("Enter Date(YYYY/MM/DD): ")
    sql = "insert into BOOK_SUBMIT values(%s,%s,%s,%s)"
    data = (BOOK_NAME,BOOK_CODE,ENROLLMENT_NUMBER,DATE)
    c = mydb.cursor()
    c.execute(sql,data)
    mydb.commit()
    print("________________________________________________________________________________")
    print("BOOK SUBMITTED FROM: ",name)
    Book_Update(code,1)

#Book Update function to update the Books table when user Issue/Submit Book
def Book_Update(code,u):
    sql = "select QUANTITY from BOOK where BOOK_CODE = %s"
    data = (code,)
    c = mydb.cursor()
    c.execute(sql,data)
    myresult = c.fetchone()
    total = myresult[0]+ u
    sql = "update Books set Total_Book = %s where Book_code = %s"
    d = (total,code)
    c.execute(sql,d)
    mydb.commit()
    main()

#Delete Book function to delete any book in library by entering Book Code
def Delete_Book():
    a = input("Enter book code: ")
    sql = "delete from BOOK where BOOK_CODE = %s"
    data = (a,)
    c = mydb.cursor()
    c.execute(sql,data)
    mydb.commit()
    print("-----RECORD UPDATED SUCCESSFULLY------")
    main()

#To Display all the rows/data of Books table
def Display_Books():
    sql = "select * from BOOK"
    c = mydb.cursor()
    c.execute(sql)
    myresult = c.fetchall()
    for i in myresult:
        print("Book Name: ",i[0])
        print("Book Code: ",i[1])
        print("Total: ",i[2])
        print("Subject: ",i[3])
        print("________________________________________________________________________________")

    main()

#Login Function
def login(users):
    while True:
        username = input("\nPlease enter allotted username: ")
        password = input("Please enter allotted password: ")

        for u in users:
            if username == u[0] and password == u[1]:
                return username
        print("Username or Password is incorrect. Please try again!")

users = [['San','1234'],['San Dynamic','hello']]

username = login(users)

print("\n",username, "has successfully logged in \n Access Accomplished :)\n")
main()
