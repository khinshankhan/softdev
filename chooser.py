import random

CLASSES = {
    7: [ 'Helen', 'Shakil', 'Eric', 'Jennifer Y', 'Jennifer Z', 'Arif', 'Queenie', 'Jawadul', 'Shaina', 'Vivien', 'Brian', 'Naotaka', 'Bayan', 'Adam', 'Caleb', 'Terry', 'Jason', 'Alessandro', 'Samantha', 'Carol', 'Joyce', 'Shannon', 'Charles', 'Taylor', 'Kelly', 'Leo', 'Khyber', 'Ibnul', 'Eugene', 'Yuyang', 'Karina', 'Tiffany', 'Holden', 'Michael'],
    8: ['Masha', 'Adrian', 'David', 'Eric', 'Josh', 'Jerome', 'Henry', 'Jackie', 'Giorgio', 'Karen', 'Sonal', 'Xavier', 'Bermet', 'Alex', 'Iris', 'Manahal', 'Donia', 'Md', 'Connie', 'Lisa', 'Xing', 'Angelica', 'Angel', 'Augie', 'Dimitriy', 'Yiduo', 'Gordon', 'Tiffany', 'Clive', 'Jonathan', 'Sasha', 'Daniel'],
    9: [ 'Yu Qi', 'Michela', 'Kristin', 'Fabiha', 'Maxim', 'Marcus', 'Ish', 'James', 'Ryan', 'Edward', 'Adeeb', 'Jake', 'Cynthia', 'Kevin', 'Levi', 'Edmond', 'Kyle', 'Andrew', 'Max', 'Jenny', 'Philip', 'Shan', 'Mansour', 'Ray', 'Jake', 'Ida', 'Kerry', 'Stanley', 'Jackie', 'William', 'Tina', 'Michael']
}

#print("hi")
#print (len(CLASSES.get(7,'oh')))
#print (len(CLASSES.get(8,'oh')))
#print (len(CLASSES.get(9,'oh')))
#print (len(CLASSES[7]))
#print (len(CLASSES[8]))
#print (len(CLASSES[9]))
#print random.randint(0,len(CLASSES.get(7,'oh')))
#print random.randint(0,len(CLASSES[7]))

while True:
    while True:
        period = raw_input("From which period do you want the random name? (7,8,9)")
        if int(period)==7 : break
        if int(period)==8 : break
        if int(period)==9 : break
    print(CLASSES[int(period)][random.randint(0,len(CLASSES[int(period)])-1)])

