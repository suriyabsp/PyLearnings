file = open('Read.txt')
#Reads all the content of the file

#print(file.read(8))


#reads by lined

print(file.readline())

print(file.readline())

# Print line by line using readline
line = file.readline()
while line!= "":
    print(line)
    line = file.readline()

for line in file.readlines():
    print(line)

file.close()