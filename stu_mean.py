import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#CODE FOR db_builder.py
#I put it here to make testing easier

c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);")

with open('courses.csv') as csvfile:
    courses_file = csv.DictReader(csvfile)
    for row in courses_file:
        c.execute("INSERT INTO courses VALUES(\'" + row["code"] + "\', " + row['mark'] + "," + row['id'] + ");")
	
c.execute("CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER PRIMARY KEY);")

with open('peeps.csv') as csvfile:
    peeps_file = csv.DictReader(csvfile)
    for row in peeps_file:
        c.execute("INSERT INTO peeps VALUES(\'" + row["name"] + "\', " + row['age'] + "," + row['id'] + ");")

#==========================================================
#ACTUAL CODE FOR stu_mean.py

#LOOK UP EACH STUDENT'S GRADES
def findGrades(name):
	c.execute("SELECT name, peeps.id, code, mark FROM peeps, courses WHERE peeps.id = courses.id AND name = '%s';" % (name))
	rows = c.fetchall()
	return rows;

#COMPUTE EACH STUDENT'S AVERAGE
def findAverage(name):
    grades = findGrades(name)
    sum = 0.0; 
    counter = 0;
    for each in grades:
        sum += each[3];
        counter += 1;
    return sum / counter;

#DISPLAY EACH STUDENT'S NAME, ID, AND AVERAGE
def display(name):
    c.execute("SELECT * FROM peeps WHERE name = '%s'"  %(name))
    row = c.fetchall()
    display = name + ", " + str(row[0][2]) + ", " + str(findAverage(name))
    return display
	
print display('alison')

#CREATE A TABLE OF IDS AND ASSOCIATED AVERAGES, NAMED "peeps_avg"
c.execute("CREATE TABLE peeps_avg (id INTEGER PRIMARY KEY, average NUMERIC)")
def peeps_avg_insert():
    c.execute("DELETE FROM peeps_avg")
    c.execute("SELECT * FROM peeps")
    rows = c.fetchall()
    for each in rows:
        c.execute("INSERT INTO peeps_avg VALUES (%d, %r)" % (each[2], findAverage(each[0])))
peeps_avg_insert()

#FACILITATE UPDATING A STUDENT'S AVERAGE
def update(id, course, new):
    c.execute("UPDATE courses SET mark = " + str(new) + " WHERE id = " + str(id) + ' AND code = "' + course + '";')
    peeps_avg_insert()
	
#FACILITATE ADDING ROWS TO THE courses TABLE
def adding(code, mark, id):
    c.execute('INSERT INTO courses VALUES ("%s", %d, %d)' % (code, mark, id))
    peeps_avg_insert()

#==========================================================
db.commit() #save changes
db.close()  #close database