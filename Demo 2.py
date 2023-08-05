#LIST datatypes and working with Examples
values = [1, 2, "Brezza", 4, 5]
#List is a datatype that allows multiple values with different datatypes

print(values[0])  #prints 1 as the datatype starts with 0

print(values[2]) #prints Brezza

print(values[3]) #prints 4

print(values[-1]) #prints last value

print(values[1:3]) #prints from 2 to 4 with Brezza

values.insert(3,'2016') #Inserts 2016 after Brezza
print(values)

values.append("ZDI+")
print(values) #prints all by adding ZDI+ in the end

values[2] = "brezza"
print(values) #prints the new upodate

del values[0]
print(values) #prints everything after deleting 1

#TUPLE datatype with example and working same as list but immutable(cannot be updated2

val = (1, 2, 'Brezza', 5.5)
print(val)

#dictionary datatype

dic = {"a": 2, 2:"xyz"}
print(dic["a"])
print(dic[2])

#inserting datas into dictionary

dict = {}

dict["Firstname"] = "Virat"
dict["Lastname"] = "Kohli"
dict["Gender"] = "Male"
print(dict)
