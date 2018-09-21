import os

def rename_files():
    #Retrieve file list
    file_path = r"C:\Python27\Udacity Projects\Secret Message\alphabet"
    file_list = os.listdir(file_path)
    print (file_list)

    #Rename files
    cwd = os.getcwd()
    os.chdir(file_path)
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None,"0123456789"))
        print "Old file name " +file_name
        print "New file name " +file_name.translate(None,"0123456789")
    os.chdir(cwd)
rename_files()
