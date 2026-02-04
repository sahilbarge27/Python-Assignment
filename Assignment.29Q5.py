filename = input("enter file name : ")
word = input("Enter string to search : ")

f = open(filename,"r")
data = f.read()

count = data.count(word)

print(word,"appears",count,"times in",filename)

f.close()