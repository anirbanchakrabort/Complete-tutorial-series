"""“a file is a resource for saving data and information in computer hardware”. 
A file is stored in the form of bytes in hardware. 
A file is opened in the RAM, but it is stored in the hardware because the hardware is non-volatile i.e. it stores its data permanently. 
On the other hand, RAM is volatile, it loses its data when the system is shut down.

Whenever we create a new file and opened the file it opened in the "read(r)" mode which is the
defsult mode. We can use the "rt" mode which is used to read text file and also
in "rb" mode which is binary mode as well . 

We can use the read(size) method which prints the first two character and aslo readlines
method which will print the entire lines of character in a file

file-modes in python

r - r mode open the files in the read mode . We do not have permission to change or update 
any text in this mode. (default)

w - wrtie mode allows us to write in the file

b - this is the binary mode in which we can read binary files like image etc

a - stands for apend,which means to something to the end the file.

t - is used to open our file in text mode.(default)

x - is used to create a new file

+ - we can read and write simustiniously


"""
#opening the file and reading the content of the file in read mode

# f = open("file.txt","r")
# content = f.read()
# print(content)

# write in the file

# f = open("file.txt","w")
# print(f.write("write mode is used to write text in a files but it will override the entire line\n"))

#read and write in the file simultiniously

# f = open("file.txt","r+")
# print(f.read())
# print(f.write("Jiobn\n"))

#appand a file

# f = open("file.txt","a")
# print(f.write("apend is used to write a text at the end of a line\n"))
