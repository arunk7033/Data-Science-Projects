import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()

mycursor.execute("""insert into ineuron.fsds values(123, 'Arun', 'Kumar','2022-11-11', 'sql', 'fsds'),
(124, 'Varun', 'Kumar','2022-11-11', 'sql', 'fsds'),
(125, 'Vicky', 'Kumari','2022-11-11', 'sql', 'fsds'),
(126, 'Ashish', 'Kumar','2022-11-11', 'sql', 'fsds'),
(127, 'Karan', 'Singh','2022-11-11', 'sql', 'fsds'),
(128, 'Ankit', 'Kumar','2022-11-11', 'sql', 'fsds'),
(129, 'Akash', 'Solanki','2022-11-11', 'sql', 'fsds'),
(130, 'Ram', 'Sagar','2022-11-11', 'sql', 'fsds')""")

mydb.commit()

mycursor.execute("select * from ineuron.fsds")

for i in mycursor:
    print(i)