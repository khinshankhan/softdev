import re
import copy
import random

data = {} #will be the dict
second = () #lists tuples of dict to be used for weights
rand = 0.0 #will be random float to see which to choose

# method to turn csv into dict
def reader (textfile):
    input_file = open(textfile,'r')
    input_dict = {}
    for line in input_file:
        if line[0:1] == "\"" :
            info = re.split("\",|\r|\n", line)
            input_dict.update({info[0][1:]: float(info[1])})
        else :
            info = re.split(",|\r|\n", line)
            if info[0] == "Total" or info[0] == "Job Class":
                continue
            else:
                input_dict.update({info[0]: float(info[1])})
                continue
    input_file.close()
    return input_dict

data = reader('data/occupations.csv')
temp = copy.deepcopy(data) #separating references
second = sorted(temp.items())

#debug
'''
#x = 0
for keys,values in data.items():
    print(keys)
    print(values)
#    x += 1
#print "Tally of entries: %s" % x
'''

percent = 0 #accumulate percents
ticker = 0 #keep place in list of tuples

#rewrites second with percent ranges
for k,v in second:
    percent = percent + v
    #print percent
    second[ticker] = (second[ticker][0],round(percent,1))
    #print second[ticker]
    ticker+= 1

#debug
'''
for k,v in second:
    print k
    print v
'''


#for test.sh
'''
file = open("dict.txt","w")
for k,v in second:
    file.write(k+'\n')
file.close()
'''
    

#method for random job
def choosejob():
    job = "ERROR" #will be changed to job
    rand = round(random.uniform(0, 99.8),1)
    #print rand
    for k,v in second:
        if rand > v:
            continue
        else:
            job = k
            break
    return job

print choosejob()

