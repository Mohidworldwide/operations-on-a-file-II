# #activity 1

# with open('codingal.txt','w') as file:
#     file.write("Hi! i am penguin and i am 1 year old")
# file.close()

# with open('codingal.txt','r') as file:
#     data=file.readlines()
#     print("words in this file are....")
#     for line in data:
#         word=line.split()
#         print(word)
# file.close()

#activity 2

my_file=open('myfile.txt','x')
my_file.close()


import os
print("checking if my_file exists or not...")
if os.path.exists("remove.txt"):
    os.remove ("remove.txt")
else:
    print("the file does not exist.")

my_file=open('my_file.txt','w')
my_file.write("Hi! i am penguin and i am 1 year old")

my_file.close()

os.remove('codingal.txt')

os.rdmir('folder')

