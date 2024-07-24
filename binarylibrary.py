import pickle

def createfile():
    o=open(r"/home/naydu420/Desktop/book.dat","ab")
    #bookno,bookname,autor,price
    bookno=int(input("Enter book no --> "))
    bookname=input("Enter book name --> ")
    author=input("Enter Author name --> ")
    price=int(input("Enter price of the Book "))
    l=[bookno,bookname,author,price]
    pickle.dump(l,o)
    o.close()
    
def read():
    o=open(r"/home/naydu420/Desktop/book.dat","rb")
    try:
        while True:
            r=pickle.load(o)
            print(r)
    except EOFError:
        o.close()
    
def countrec(Author):
    o=open(r"/home/naydu420/Desktop/book.dat","rb")
    n=0
    try:
        while True:
            r=pickle.load(o)
            if Author.capitalize()==r[2]:
                n+=1
    except EOFError:
        o.close()
    n1=("No. of book currently available of the author is/are --> ",n)
    return n1 

def searchbook(book):
    o=open(r"/home/naydu420/Desktop/book.dat","rb")
    try:
       
        while True:
            r=pickle.load(o)
            if book.capitalize()==r[1]:
                p=r[3]
                print("Book price before change--> ",p)
                print("Press 1 to decrease price ")
                print("Press 2 to increase price ")
                e=int(input("Enter your choice --> "))
                if e==1:
                    p-=5
                if e==2:
                    p+=15
                z=("Book price is :- ",p)
                
        else:
            print("No related Book found!")        
        
    except EOFError:
        o.close()
    return z
    
rea=input("Want to display the content of file (Y/N) ")
if rea.lower() in 'y'or'yes':
    read()   
q=input("Which Author's book you want to search: ")
if True:
    print(countrec(q))
x=input("Which Book Price You Wanna Search: ")
if True:
    print(searchbook(x))                
