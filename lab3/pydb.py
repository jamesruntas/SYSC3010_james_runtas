#!/usr/bin/env python3
import sqlite3
#connect to database file
dbconnect = sqlite3.connect("mydatabase.db");
dbconnect.row_factory = sqlite3.Row;
#now we create a cursor to work with db
cursor = dbconnect.cursor();
#execute insetr statement
cursor.execute('''insert into temps values ('2020-9-29', '11:50:00', 'python', 26.0)''');
dbconnect.commit();
#execute simple select statement
cursor.execute('SELECT * FROM temps');
#print data
for row in cursor:
    print(row['ttime'],row['temperature'],row['tdate'] );
#close the connection
dbconnect.close();
