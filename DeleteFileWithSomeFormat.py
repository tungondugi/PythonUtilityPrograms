# This program will delete the files that I don't want having some formats like, .CR2??
import os
# import sys

def deleteFile(directoryPath, fileExtension):
    # directoryPath = "E:\Photos\Gekha_Family_Branch_Picnic_2021"


    # changing to that directory
    os.chdir(directoryPath)
    # Listing the files
    FileList = os.listdir()

    # list of type of file extension(s) I want to delete
    # deleteExtension = ['.CR2']

    # I will split the filename and the file format using splittext() in os module
    for files in FileList:
        # Let's ignore the directories
        if os.path.isdir(files):
            pass
        else:
            # splitting the fileName and the fileFormat using splittext() in os module
            # this will give a tuple of filename and the fileformat
            fileName, fileFormat = os.path.splitext(os.path.basename(files))
            if fileFormat in fileExtension:
                # if true then delete the file
                os.remove(files)

if __name__ == '__main__':
    directoryPath = r"E:\Photos\family get together\Gekha_Family_Branch_Picnic_2021"
    fileExtension = [".CR2"]

    # callback
    deleteFile(directoryPath, fileExtension)
