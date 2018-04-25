lc = [chr(ord('a')+i) for i in range(0,26)] #lowercases
uc = [chr(ord('A')+i) for i in range(0,26)] #uppercases
nac = '. ? ! & # , ; : - _ *' #non-alphanumeric chars

#returns true if string contains a mixture of
#upper- and lowercase letters, and at least one number
def Alphanumeric(string):
    return True in [ c in uc for c in string ] and True in [ c in lc for c in string ] and True in [c.isdigit() for c in string ]

#return a lower integer for a weak password and a
#higher integer for a stronger password (Suggested scale: 1-10)
def strength(string):
    if (Alphanumeric(string) and hasNAC(string)):
        return 10
    elif (Alphanumeric(string)):
        return 8
    elif ((Alpha(string) or Anum(string) or anum(string)) and hasNAC(string)):
        return 7
    elif (Alpha(string) or Anum(string) or anum(string)):
        return 4
    else:
        return 1

#helper methods
def Alpha(string):
    return True in [ c in uc for c in string ] and True in [ c in lc for c in string ]

def Anum(string):
    return True in [ c in uc for c in string ] and True in [c.isdigit() for c in string ]

def anum(string):
    return True in [ c in lc for c in string ] and True in [c.isdigit() for c in string ]

def hasNAC(string):
    g = [1 for c in string if c in nac]
    return True if 1 in g else False

#Testing minimum threshold
print Alphanumeric('Hi') #false
print Alphanumeric('i') #false
print Alphanumeric('I') #false
print Alphanumeric('G6') #false
print Alphanumeric('a4') #false
print Alphanumeric('Qw5') #true
#Testing Strength
print strength('A') #1
print strength('b') #1
print strength('1') #1
print strength('1.') #1
print strength('a1.') #7
print strength('A1.') #7
print strength('Ab') #4
print strength('Ab1') #8
print strength('Ab.1') #10
