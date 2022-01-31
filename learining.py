


from cmath import log


yuval = "yuval"
studnets = [yuval, "gabi", "tsori", "noam"]
grades = (100, 50, 20)

# slice
print(studnets[2:4]) #['tsori', 'noam']
print(studnets[::-1]) #['noam', 'tsori', 'gabi', 'yuval']
print(studnets[-1])
print(studnets.count("yuval"))
print(87 in grades)
for student in studnets:
    print(f"I am {student.upper()}")
    print(f"I am {student[::-1]}")
bla = (34, "blabla", True, 67.5)


# function
def div_mode(a,b):
    return a//b, a % b
print(div_mode(*(13,4))) # Create tuple

# Distract
a, b = div_mode(13,9)
print(a,b)

# Extends
l= [1,2,3]
l.extend((1,2,3))
print(l)

# Immutable: str, tuple
# mutable: list, dict, set


# set
js_team = {"elay", "oryan", "shaked", "ido"}
py_team = {"gabi", "aviv", "noam", "ido"}

print("ido" in py_team)
print(js_team.intersection(py_team))
print(js_team.issuperset(("shaked", "oryan")))
print(js_team.intersection(("shaked", "oryan")))
print(js_team.union(py_team))


# Dict
grades = {"ido": 76, "or":80, "yam":92}
print("yuval" in grades)
print(grades.values())
print(grades.keys())
print(grades.items())

for key,value in grades.items():
    print(f"im {key} and i got {value}")

i=0
for student in studnets:
    i+=1
    print(f"{i}: {student}")


for i,student in enumerate(studnets):
    i+=1
    print(f"{i}: {student}")


# Spread
a,*c = "abcdefg"
print(*c)
l=[1,2,3]
print([4,5,*l])
def product(*numbers):
    prod = 1
    for num in numbers:
        prod*=num
    return prod
print(product(1,2,3,4,5))


# Comprehension
defaultList = []
for i in range(12):
    defaultList.append(i)

poweredList = [100*i for i in range(12)]
print(poweredList)

newPoweredList = [2 ** i for i in range(12) if 2 ** i > 100]
print(newPoweredList)

newStudnets = [student for student in studnets if "i" in student.lower()]
print(newStudnets)

newIndexStudents = [student for index, student in enumerate(studnets) if index % 2 == 0]
print(newIndexStudents)


# build in functions:
# map, filter, all, any, zip, min, max, abs, round, sum, hash, sorted, reversed

# lambda 
newLambda = [*filter(lambda n: n > 100, map(lambda i: 2 ** i, range(12)) )]
print(newLambda)