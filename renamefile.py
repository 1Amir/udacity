import os, sys
#Open a file
def renamefile():
    file_list = os.listdir("/home/amir/udacity/renamefileproject")
    print file_list

    #Rename all the files.
    os.chdir("/home/amir/udacity/renamefileproject")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
	print file_name
renamefile()  
