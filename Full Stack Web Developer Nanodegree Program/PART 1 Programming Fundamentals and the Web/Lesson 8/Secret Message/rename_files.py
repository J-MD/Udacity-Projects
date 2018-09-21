import os

def rename_files():
    #Retrieve file list
    file_list = os.listdir(r"C:\Python27\Udacity Projects\Secret Message\prank")
    print (file_list)

    #Rename files
    cwd = os.getcwd()
    os.chdir(r"C:\Python27\Udacity Projects\Secret Message\prank")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None,"0123456789"))
        print "Old file name" +file_name
        print "New file name" +file_name.translate(None,"0123456789")
    os.chdir(cwd)
rename_files()
