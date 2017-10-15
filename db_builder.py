import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
def builder(textfile,args): #going to assume it's csv and make do without .csv in argument
    data = open(textfile+".csv", "r")
    peeps = csv.DictReader(data)
    headers = peeps.fieldnames
    command = "CREATE TABLE %s (%s);" %(textfile, args)
    #print command
    c.execute(command)
    for row in peeps:
        values = '('
        for name in headers:
            if name != 'name' and name != 'code':
                values += row[name]+', '
            else:
                values += '"' + row[name]+'", '
        values = values[:-2]
        values += ')'
        #print values
        insertion = "INSERT INTO %s VALUES " %textfile
        c.execute(insertion + values) #run SQL statement
    data.close()
    return

builder("peeps", "name STRING, age INTEGER, id INTEGER PRIMARY KEY")
builder("courses", "code TEXT, mark INTEGER, id INTEGER")

#==========================================================
db.commit() #save changes
db.close()  #close database


