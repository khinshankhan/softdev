def union(set1, set2):
    return [i for i in set1 if i not in set2] + [i for i in set2 if i not in set1] + [i for i in set2 if i in set1]

def intersect(set1, set2):
 return  [i for i in set2 if i in set1]

def setDifference(set1, set2):
    return [i for i in set1 if i not in set2]

def symmetricDifference(set1, set2):
    return [i for i in set1 if i not in set2] + [i for i in set2 if i not in set1]

def cartesianProduct(set1, set2):
    return [[i, j] for i in set1 for j in set2]
    
#Testing union
set1 = [1,2,3]
set2 = [2,3,4]
print union(set1, set2)
print intersect(set1, set2)
set1 = [1, 2, 3]
set2 = [2, 3, 4]
print setDifference(set1, set2)
set1 =  [2, 3, 4]
set2 = [1, 2, 3]
print setDifference(set1, set2)
print symmetricDifference(set2, set1)
set1 = [1,2,3]
set2 = ['a','b','c']
print cartesianProduct(set1, set2)
set2 = ['a','b']
print cartesianProduct(set1, set2)

