import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    passwd="root",
    database="testdatabase"
)

mycursor = db.cursor()

# mycursor.execute("CREATE TABLE Person(name varchar(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

# mycursor.execute("INSERT INTO Person(name, age) values ('Filora',31)")
# db.commit()
# mycursor.execute("CREATE TABLE Test (name varchar (50) NOT NULL, created datetime, gender ENUM('M', 'F', 'O') NOT NULL, id int primary key not null AUTO_INCREMENT)")

# mycursor.execute("INSERT INTO Test(name, created, gender) values ('Elshat', current_time,'M')")
# db.commit()

# mycursor.execute("select name from Test where gender = 'F' order by id desc ")

#for x in mycursor:
 #   print(x)

# mycursor.execute("alter table Test add column food varchar(50) not null ")

mycursor.execute("Alter table Test change first_name first_name varchar(6)")

mycursor.execute("describe Test")

for x in mycursor:
    print(x)



