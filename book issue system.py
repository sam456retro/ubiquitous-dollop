import time
import sys
import os
def welcome_screen():                     #welcome screen
    print("\n\n\n\n\n\n--------------------------------WELCOME TO BAL BHARATI PUBLIC SCHOOL LIBRARY MANAGEMENT SYSTEM-----------------------------------\n")
    print("-------------------------------------------------library management system:version 2.0-----------------------------------------")

class screens():
    
    def cls():                            #clear screen
        print("\n" * 50)

    def exit():                           #confirm exit
        screens.cls()
        print("are you sure you want to leave ?")
        while True:
            try:
                e = str(input("y or n: "))
                e = e.lower()
                if e == "y" or e == "n":
                    break
                else:
                    print("only y or n please !!!!!")
            except:
                print("only alphabets please!!!")
        if e == "y":
            screens.cls()
            sys.exit() 
        else:
            screens.start_screen()
    
    def start_screen():                    #choice
        screens.cls()
        print("-------------------------------------------welcome to book entry system --------------------------------\n")
        print(" 1. issue ")
        print(" 2. deposit")
        print(" 3. veiw all issued books")
        print(" 4. all books")
        print(" 5. admin menu")
        print(" 6. exit\n")
        while True:
            try:
                choice = int(input("enter the choice you want:  "))
                if choice > 6 or choice == 0:
                    print("only less than 7 please!!!!!!")
                else:
                    break
            except:
                print("only numbers please!!!!!!")
        if choice == 1:
            library.issue()
            time.sleep(1)
            screens.start_screen()
        elif choice == 2:
            library.deposit()
            time.sleep(1)
            screens.start_screen()
        elif choice == 3:
            library.issued_all()
            time.sleep(3)
            screens.start_screen()
        elif choice == 4:
            book.all_view()
            time.sleep(3)
            screens.start_screen()
        elif choice ==  5:
            admin.login()
        else:
            screens.exit()

class admin():
    def admin_menu():                                        #admin options
        screens.cls()
        print("-------------------------------------------------admin menu ----------------------------------------------\n")
        print("1. new book record ")
        print("2. all book records")
        print("3. new student reacord")
        print("4. all student records")
        print("5. delete menu")
        print("6. factory reset")
        print("7. return to issueing screen\n")
        while True:
            try:
                admin_choice = int(input("enter your choice: "))
                if admin_choice > 7 or admin_choice == 0:
                    print("only  from 1 - 7 choices !!!!")
                else:
                    break
            except:
                print("only numbers allowed!!!!!")
        if admin_choice == 1:
            book.book_entry()
            time.sleep(1)
            admin.admin_menu()
        elif admin_choice == 2:
            book.all_view()
            time.sleep(3)
            admin.admin_menu()
        elif admin_choice == 3:
            student.student_entry()
            time.sleep(1)
            admin.admin_menu()
        elif admin_choice == 4:
            student.student_all()
            time.sleep(3)
            admin.admin_menu()
        elif admin_choice == 5:
            admin.delete_screen()
        elif admin_choice == 6:
            admin.factory_comfirmation()
        else:
            screens.start_screen()
    
    def login():                              #admin login
        screens.cls()
        while True:
            try:
                aname = str(input("enter user name:  "))
                pname = str(input("enter password:   "))
                break
            except:
                print("only words please!!!!!")
        if aname == "program" and pname == "python":
            admin.admin_menu()
        else:
            print("wrong password or username!!!")
            time.sleep(1)
            screens.start_screen()

    def delete_screen():                     #to delete records
        screens.cls()
        print("--------------------------------delete-----------------------------")
        print("\n 1. delete student record")
        print(" 2. delete book record")
        print(" 3. go back to Admin Menu\n")
        while True:
            try:
                cchoice = int(input("enter your choice:  "))
                if cchoice == 0 or cchoice > 3:
                    print("only less then 4 allowed!")
                else:
                    break
            except:
                print("only numbers allowed!")
        if cchoice == 1:
            student.student_remove()
            time.sleep(1)
            admin.delete_screen()
        elif cchoice == 2:
            book.book_remove()
            time.sleep(1)
            admin.delete_screen()
        else:
            admin.admin_menu()

    def factory_comfirmation():                                   #confirm reset
        screens.cls()
        print("\n\n\n\n\n")
        print("are you sure you want to reset all files?")
        print("after this no data will be left!")
        while True:
            try:
                fchoice = str(input("enter yes or no:  "))
                fchoice = fchoice.lower()
                if fchoice == "y" or fchoice == "n":
                    break
                else:
                    print("only yes or no please!!!!")
            except:
                print("only y or n please!!")
        if fchoice == "y":
            admin.factory_reset()
        else:
            admin.admin_menu()
    
    def factory_reset():                     #reset all records 
        f20 = open("book.dat","w")
        f30 = open("issued.dat","w")
        f40 = open("student.dat","w")
        f20.close()
        f30.close()
        f40.close()
        print("RESET ALL FILES! NO DATA LEFT!")
        time.sleep(1)
        main()
        
class student():
    def student_entry():                      #new student entry
        screens.cls()
        while True:
            try:
                sname = str(input("enter student name: "))
                sadmin = int(input("enter student admission number: "))
                break
            except:
                print("only names please!!!!!!")
        f2 = open("student.dat","a")
        f2.write(str(sadmin) + "\t" + sname + "\n") 
        f2.close()
        print("DETAILS SAVED!")

    def student_all():                           #all student records
        screens.cls()
        print("----------------------------------------------------Data----------------------------------------------\n")
        f3 = open("student.dat","r")
        print(f3.read()) 
        f3.close()

    def student_remove():                        #remive student record
        screens.cls()
        while True:
            try:
                gname = int(input("enter admission number of student:  "))
                break
            except:
                print("only the addmission number please!!!!")
        f12 = open("student.dat","r")
        f13 = open("temp.dat","w")
        for line in f12:
            if str(gname) in line:
                continue
            else:
                f13.writelines(f12.readlines())
        f12.close()
        f13.close()
        os.remove("student.dat")
        os.rename("temp.dat","student.dat")

class book():
    def book_entry():            #to make a new entry
        screens.cls()
        while True:
            try:
                name = str(input("enter book name: "))
                author = str(input("enter author name: "))
                break
            except:
                print("only the names please!!!!!!")
        f = open("book.dat","a")
        f.write(name+"\t" + "by" + "\t" +author + "\n")
        f.close()
        print("SAVED THE DETAILS!!!!!!!")

    def book_remove():                        #remove book record
        screens.cls()
        while True:
            try:
                gname = str(input("enter book name:  "))
                break
            except:
                print("only the book name please!!!!")
        f12 = open("book.dat","r")
        f13 = open("temp.dat","w")
        for line in f12:
            if str(gname) in line:
                continue
            else:
                f13.writelines(f12.readlines())
        f12.close()
        f13.close()
        os.remove("book.dat")
        os.rename("temp.dat","book.dat")
    
    def all_view():                          #to veiw all book records
        screens.cls()
        f1 = open("book.dat","r")
        print("----------------------------------------------------Data----------------------------------------------\n")
        print(f1.read())
        f1.close()

class library():

    def issue():                                   #issue book
        screens.cls()
        while True:
            try:
                dname = int(input('admission number:  '))
                ename = str(input("book issueing: "))
                break
            except:
                print("please fill in the right details!!!")
        found3 = bool()
        found3 = False
        datafile1 = open('issued.dat',"r")
        found3 = False
        for line in datafile1:
            if ename in line:
                found3 = True
                break
            else: 
                found3 = False
                break
        
        found = bool()
        found = False
        datafile = open('issued.dat',"r")
        found = False
        for line in datafile:
            if str(dname) in line:
                found = True
                break
            else: 
                found = False
                break
        
        found1 = bool()
        found1 = False
        f7 = open('book.dat','r')
        found1 = False
        for line in f7:
            if ename in line:
                found1 = True
                break
            else:
                found1 = False
                break    
            
        found2 = bool()
        found2 = False
        f8 = open('student.dat','r')
        found2 = False
        for line in f8:
            if str(dname) in line:
                found2 = True
                break
            else:
                found2 = False
                break     
        
        if found == True:
            print("1 book is already with the child. please return that first!")
        elif found1 == False:
            print("no such book present")
        elif found2 == False:
            print("no student with such number")
        elif found3 == True:
            print("book already issued by another student")
        else:
            f5 = open("issued.dat","a")
            f5.write(str(dname) + "\t\t" + ename + "\n")
            f5.close()
    
    def deposit():                             #deposit book
        screens.cls()
        while True:
            try:
                z = int(input("enter the admission number of child:  "))
                break
            except:
                print("only the addmission number please!")
        f = open('issued.dat','r')
        f10 = open("temp.dat","w")
        while True:
            for line in f:
                if str(z) in line:
                    continue
                else:
                    f10.writelines(f.readlines(line))
            break
        f.close()
        f10.close()
        os.remove("issued.dat")
        os.rename("temp.dat","issued.dat")
             
    def issued_all():                                 #check all issued records
        screens.cls()
        print("------------------------------------------------------issued books--------------------------------------------------------\n")
        print("admin no\tbook name")
        f6 = open("issued.dat","r")
        print(f6.read())
        f6.close()

def main():                                           #main program
    screens.cls()
    welcome_screen()
    time.sleep(2)
    screens.cls()
    screens.start_screen()

if True:
    main()
