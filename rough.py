import mysql.connector as sq
import sys
import time
import random
import fontstyle
import clx.xms

#Establishing connection

def connection():
    try:
      con=sq.connect(host="localhost",user="root",password="Priyanav@1",database="Vaccine_management_system")
      if con.is_connected()==False:
          print("database not connected")
      else:
          return con
    except sq.Error as er:
      print(er)
#For checking a person is COVID-19 positive or not and inserting data in 1st table
def check():
    try:
        con = connection()
        cur = con.cursor()
        name = input("Please enter the name of the person to be vaccinated:\n")
        Result=input("Enter the test result(positive/negative):(p/n)")
        chedat=(name,Result)
        cur.execute("insert into test values(%s,%s)",chedat)
        print("data inserted successfully")
        con.commit()
    except sq.Error as er:
        print(er)

def display1():
    try:
        con=connection()
        cur=con.cursor()
        cur.execute("select * from test")
        for i in cur.fetchall():
            print(i)
    except sq.Error as er:
        print(er)

def deletion1():
    try:
        con = connection()
        cur = con.cursor()
        name = input("Please enter the name of the person to be deleted from database:\n")
        cur.execute("delete from test where name= %s"%(name))
        print()
        con.commit()
        print("Data Deleted successfully")
    except sq.Error as er:
        print(er)

#For slowing down the speed of ASCII art to make it more user friendly and convenient
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./8)

#Inserting data in 2nd table vaccine
def insertion():
    try:
        con=connection()
        cur=con.cursor()
        nurname = input("Enter your name as a nurse:\n")
        global name
        name = input("Please enter the name of the person to be vaccinated:\n")
        global Aadharno
        Aadharno = input("Please enter the aadhaar no. of the person:\n ")
        Regmobileno = input("Please enter the registered mobile no. with +91:\n ")
        Secode = input("Enter the secret code of the person:\n ")
        global DOB
        DOB = input("Enter your dob:\n")
        year = ""
        for i in range(6, 10):
            year += DOB[i]
        global age
        age = 2022 - int(year)
        vadat = (nurname, name, Aadharno, Regmobileno, Secode, DOB, age)
        cur.execute("insert into vaccine(nurname, name, Aadharno, Regmobileno, Secode, DOB, age) values('%s','%s','%s','%s','%s','%s','%s')"%vadat)
        print("data inserted successfully")
        con.commit()
    except sq.Error as er:
        print(er)
    client = clx.xms.Client('ab9cafb12e0845f6a3b1124fe84fb45d', 'dad4876194f649d88627d2539b310e67')
    client.create_text_message(
        sender='+447520651637',
        recipient=Regmobileno,
        body='This is test message for Sinch')
    print("You'll receive a confirmation message shortly")

#Updating data in table vaccine
def updation():
    try:
        con=connection()
        cur=con.cursor()
        name = input("Please enter the name of the person whose name you wanted to change:\n")
        Aadharno = input("Please enter the aadhaar no. of the person:\n ")
        Regmobileno = input("Please enter the registered mobile no. with +91:\n ")
        Secode = input("Enter the secret code of the person:\n ")
        age=input("Enter the age of the person: ")
        cur.execute("update vaccine set name='%s',Regmobileno='%s', Secode='%s', age='%s' where Aadharno= '%s'")
        print()
        con.commit()

        print("data updated successfully")

    except sq.Error as er:
        print(er)

#Displaying data from 1st table vaccine
def display2():
    try:
        con=connection()
        cur=con.cursor()
        cur.execute("select * from vaccine")
        for i in cur.fetchall():
            print(i)
    except sq.Error as er:
        print(er)

#Deletion of a record from 1st table vaccine
def deletion2():
    try:
        con = connection()
        cur = con.cursor()
        Aadharno = input("Please enter Aadhar number of the person to be deleted from database:\n")
        cur.execute("delete from vaccine where Aadharno= %s"%(Aadharno))
        print()
        con.commit()
        print("Data Deleted successfully")
    except sq.Error as er:
        print(er)

#Inserting data in 2nd table dose
def insertion2():
    try:
        con = connection()
        cur = con.cursor()
        dose = input("Is this your first/second dose:(f/s). If none of the given press ENTER\n")
        FLW = "n"
        if dose == "f":
            dose = "first"
        elif dose == "s":
            dose = "second"
        elif dose != "f" and dose != "s":
            FLW = input("Are you a front line worker:(y/n)\n")
        vaccine15_18 = ["Covaxin", "ZyCoV-1", "Pfizer-BioNTech", "Pfizer", "Moderna", "Sinovac", "Sinopharm"]
        vaccine18nabove = ["Covishield", "Covaxin", "Pfizer", "Moderna", "Johnson & Johnson"]
        r1518 = random.choice(vaccine15_18)
        r18na = random.choice(vaccine18nabove)
        r15 = fontstyle.apply(r1518, 'bold/Blink/yellow/GREEN_BG')
        r18 = fontstyle.apply(r18na, 'bold/Blink/yellow/GREEN_BG')
        vaccinename = ""
        global age
        if age >= 15 and age < 18:
            vaccinename = r15
        elif age >= 18 and FLW == "n":
            vaccinename = r18
            if age >= 15 and age < 18:
                print(f"Give them their {dose} dose of {r15} ")
            elif age >= 18 and FLW == "n":
                print(f"Give them their {dose} dose of {r18}")
            elif age >= 18 and FLW == "y":
                print(f"If they are already vaccinated with first and second dose give them booster dose of {(r18)}")
        dodat=(name,dose,vaccinename)
        cur.execute("insert into dose(name,dose,vaccinename) values('%s','%s','%s')"%dodat)
        print()
        print("data inserted successfully")
        con.commit()
    except sq.Error as er:
        print(er)

#Displaying data from 2nd table dose
def display3():
    try:
        con = connection()
        cur = con.cursor()
        cur.execute("select * from dose")
        for j in cur.fetchall():
            print(j)
    except sq.Error as er:
        print(er)
slowprint("""──▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
""")
slowprint("""^   ^   ^   ^   ^   ^   ^       ^   ^   ^   ^   ^   ^   ^   ^   ^   ^       ^   ^   ^   ^   ^   ^  
 /V\ /A\ /C\ /C\ /I\ /N\ /E\     /M\ /A\ /N\ /A\ /G\ /E\ /M\ /E\ /N\ /T\     /S\ /Y\ /S\ /T\ /E\ /M\ 
<___X___X___X___X___X___X___>   <___X___X___X___X___X___X___X___X___X___>   <___X___X___X___X___X___>
""")
exit="n"
while exit=="n":
    print("""0-Check the person is covid-19 positive or not
    1-Insert Details of a Person for vaccination
    2-Update Details of a Person in vaccine Table
    3-Display contents of vaccine table
    4-Display contents of test table
    5-Delete a Person's data from test table
    6-Delete a Person's data from vaccine table
    7-Insert Details of doses for a person
    8-Display contents of dose table
    """)
    choice=input("Enter Your Choice: ")
    if choice=="0":
        check()
    elif choice=="1":
        insertion()
    elif choice=="2":
        updation()
    elif choice=="3":
        display2()
    elif choice=="4":
        display1()
    elif choice=="5":
        deletion1()
    elif choice=="6":
        deletion2()
    elif choice=="7":
        insertion2()
    elif choice=="8":
        display3()
    exit=input("Do you want to exit?(y/n)").lower()