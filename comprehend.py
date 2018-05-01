import sys

#read file and create list, then close file
f = open ('uncletomcabin.txt', 'r')
booklist = f.read().split()
f.close

def freq(word):
    listi = filter((lambda w: word.lower() == w.lower()), booklist)
    return reduce(lambda x, y: x + 1, listi, 0)

def total_freq(wordlist):
    listfreqs = [freq(w) for w in wordlist]
    #print listfreqs
    return reduce(lambda x, y: x + y, listfreqs, 0)

#helper function
def comparator(a,b):
    #changed to set  of book
    #a.lower() == b.lower()
    return a if a > freq(b) else freq(b)

def most_freq():
    setbook = set(booklist)
    return reduce (lambda x,y: comparator(x,y), list(setbook))
    
    
#Test Cases
print "Frequency of 'email', which should be 3:", freq("email")
print "Frequency of 'archive', which should be 13:", freq("archive")
print "Frequency of 'friendos', which should be 0:", freq("friendos")
temp = ['email', 'archive']
print "Frequency of 'email' and 'archive',which should be 16:", total_freq(temp)
temp = ['email', 'friendos']
print "Frequency of 'email' and 'friendos',which should be 3:", total_freq(temp)
print "\n\nNext up is most_freq, it's SUPER SLOW...."
sys.stdout.flush()
#print freq('the')
most = most_freq()
print "Should be 'the' (7920 occurrences): %s"%most 
