# text file and binary file


# Python Image Library

# inbuilt open function
# open(filename, mode)
# Modes
# r = for reading – The file pointer is placed at the beginning of the file. This is the default mode.
# The r throws an error if the file does not exist or opens an existing file without truncating it for reading; the file pointer position at the beginning of the file.

# r+ = Opens a file for both reading and writing. The file pointer will be at the beginning of the file.
# The r+ throws an error if the file does not exist or opens an existing file without truncating it for reading and writing; the file pointer position at the beginning of the file.

# w = Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
# The w creates a new file or truncates an existing file, then opens it for writing; the file pointer position at the beginning of the file.

# w+ = Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, it creates a new file for reading and writing.
# The w+ creates a new file or truncates an existing file, then opens it for reading and writing; the file pointer position at the beginning of the file.

# rb+ = Opens a file for both reading and writing in binary format.

# rb = Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file.

# wb+ = Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, it creates a new file for reading and writing.

# a = Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
# The a creates a new file or opens an existing file for writing; the file pointer position at the end of the file.

# ab = Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.

# a+ = Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
# The a+ creates a new file or opens an existing file for reading and writing, and the file pointer position at the end of the file.

# ab+ = Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
# # x = open for exclusive creation, failing if the file already exists (Python 3)


# https://mkyong.com/python/python-difference-between-r-w-and-a-in-open/#:~:text=The%20r%20means%20reading%20file,and%20writing%20file%2C%20append%20mode.


# 	                r	r+	w	w+	a	a+
# read	            *	*		*		*
# write		            *	*	*	*	*
# create			        *	*	*	*
# truncate			        *	*
# position at start	*	*	*	*
# position at end					*	*

# P.S In this context, truncate means delete the content of the file.


# file = open("abcd.txt", "r")
# print(file.read())
# file.close()

# print("=========================================")
# file = open("abcd.txt", "r")
# print(file.read(5))
# file.seek(0)
# print(file.read(20))
# print(file.read(5))
# print(file.read(5))
# file.close()


# file = open("abcd.txt", "r")
# print(file.readline())
# print(file.readline())
# print(file.readline())
# file.close()

# file = open("abcd.txt", "r")
# print(file.readlines())
# file.close()

# print("====================================\n")


# Check this out
# file = open("abcd.txt", "r")
# the value passed to file is iterable
# print(len(file.readlines()))
# for line in file:
#     print(file.readline())
# file.close()


# f = open("abcd1.txt", "w")
# f.write("This is a testing write")
# f.close()

# f = open("abcd123.txt", "w")
# f.write("This is a testing write that is overwritten")
# f.close()

# f = open("abcd1.txt", "a")
# f.write("This is a testing write that is appended")


# f = open("cotiviti.txt", "x")
# f.write("This is a testing write that is appended")


# # deleting a file in python
# import os

# os.remove("cotiviti.txt")
# os.path.exists to check file
# os.rmdir to delete directory
# os.rename(old_file_name, new_file_name) to rename file


# f = open("abcd123.bin", "wb")
# s = str.encode("This is a testing write that is appended")
# f.write(s)


# f = open("abcd123.bin", "rb")
# data = f.read() b'This is a testing write that is appended'   b'\x36\x23\'


try:
    f = open("cotiviti.txt", "x")
except FileExistsError:
    print("File already exists")
    read = open("cotiviti.txt", "r")
    lines = len(read.readlines())
    read.close()
    f = open("cotiviti.txt", "a")
    f.write(
        f"\n This is a testing write that is appended in the line number {lines + 1}"
    )
else:
    f.write("this will be the first line number 1")
finally:
    f.close()
    print("File is closed")


# Context Manager


# f = open("cotiviti.txt", "r")


try:
    f = open("cotiviti.txt", "r")
except FileNotFoundError:
    pass
else:
    f.read()
finally:
    f.close()
