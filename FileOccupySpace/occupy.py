import re
import copy
import random

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
    return input_dict

# global var
data = reader('occupations.csv')
temp = copy.deepcopy(data)
second = sorted(temp.items())

'''
percent = 0
ticker = 0
for k,v in second:
    percent = percent + v
    #print k, percent
    #print second[ticker][1]
    print "Val: %s" % second[ticker][1]
    ticker+= 1

'''
#print second
'''
for key in data:
   print "key: %s , value: %s" % (key, data[key])
'''

rand = round(random.uniform(0, 99.8),1)
#print rand

#debug
'''
#x = 0
for keys,values in data.items():
    print(keys)
    print(values)
#    x += 1
#print "Tally of entries: %s" % x
'''
