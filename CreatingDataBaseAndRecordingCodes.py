import sqlite3

dataBase = sqlite3.connect('sportParkProject.db')
print("Data Based Opened")


# def CreateDonationsTable():
#     dataBase.execute('''
#     CREATE TABLE IF NOT EXISTS Donations(
#     DonationID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#     IBAN CHAR(26) NOT NULL,
#     NameSurname TEXT NOT NULL,
#     DonationAmount FLOAT NOT NULL
#     )
#     ''')
#
#
def createRegister():
    dataBase.execute('''
    CREATE TABLE Register(
    registerID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    TC TEXT NOT NULL,
    Name TEXT NOT NULL,
    Surname TEXT NOT NULL,
    Height TEXT NOT NULL,
    Weight TEXT NOT NULL,
    Gender TEXT NOT NULL,
    Password TEXT NOT NULL,
    Email TEXT NOT NULL,
    Phone TEXT NOT NULL
    )''')

def createSport():
    dataBase.execute('''
    CREATE TABLE Sports(
    sportID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    sportName TEXT NOT NULL,
    session TEXT NOT NULL,
    forGender TEXT NOT NULL
    )''')


def CreateTripAdviceTable():
    dataBase.execute('''
        CREATE TABLE IF NOT EXISTS TripAdvices(
        TripAdvicesID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        NameSurname TEXT NOT NULL,
        CityName TEXT NOT NULL,
        StateName TEXT NOT NULL,
        LocationsAndReasons TEXT NOT NULL
    )''')


# def CreatingAllTables():
#     CreateIdeasTable()
    # CreateDonationsTable()
    # CreateTicketsReceivedTable()
    # CreateTripAdviceTable() #Already created


# def insertSport(ID, name, session,gender):
#     dataBase.execute('''INSERT INTO Sports(sportID,sportName,session,forGender) VALUES(?,?,?,?)''',
#                      (ID, name, session,gender))
#     dataBase.commit()  # To Applying the Changes
#
#
# def insertRegister(registerID,TC,Name,Surname,Height,Weight,Gender,Password,Email,Phone):
#     dataBase.execute('''INSERT INTO Register(registerID,TC,Name,Surname,Height,Weight,Gender,Password,Email,Phone) VALUES(?,?,?,?,?,?,?,?,?,?)''',
#                      (registerID,TC,Name,Surname,Height,Weight,Gender,Password,Email,Phone))
#     dataBase.commit()  # To Applying the Changes
#
#
# def insertTripAdvice(ID, NameSurname, City, State, Reason):
#     dataBase.execute('''INSERT INTO TripAdvice(AdviceID,NameSurname,City,State,Reasons) VALUES(?,?,?,?,?)''',
#                      (ID, NameSurname, City, State, Reason))
#     dataBase.commit()  # To Applying the Changes
#
#
# def insertTicket(TicketID, IdentityNo, NameSurname, Date, Location, Class, IBAN):
#     dataBase.execute('''INSERT INTO TicketsReceived(TicketID,IdentityNo,NameSurname,Date,Location,Class,IBAN)
#     VALUES(?,?,?,?,?,?,?)''',
#                      (TicketID, IdentityNo, NameSurname, Date, Location, Class, IBAN))
#     dataBase.commit()  # To Applying the Changes
#
#
# createRegister() #Already Created
# createSport()
# insertRegister(1, "26476490554", "Ali","Baba", "181","75","Male","123321","alibaba@std.izu.edu.tr","55254525")
# insertSport(1312, "Football", "15.40 - 16.40", "Female")

dataBase.close()
print("Data Base Closed")