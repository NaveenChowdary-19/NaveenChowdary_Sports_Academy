import sqlite3
connection = sqlite3.connect("Players_database.db")

cursr = connection.cursor()

'''
cursr.execute("""CREATE TABLE Players1(
              Name text ,
              Stars integer ,
              Cricketer_Type text  )
              """)
'''
'''
cursr.execute("INSERT INTO Players1 values('Sachin Tendulkar' , 10 , 'Batsman')")
cursr.execute("INSERT INTO Players1 values('Rohith Sharma' , 10 , 'Batsman')")
cursr.execute("INSERT INTO Players1 values('Zaheer Khan' , 10 , 'Bowler')")
'''
cursr.execute("SELECT * FROM Players1 where Cricketer_Type = 'Batsman' ")

print(cursr.fetchall())

connection.commit()
connection.close()





