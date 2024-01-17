import os, shutil, re

def main()->None:

    src: str = input("Enter the source file path: ") # takes source folder path
    dst: str = input("Enter the destination file path: ") # takes destination folder path
    
    src = re.sub(r"\\", "/", src) # substitute '/' if user inputs the '\' in the input
    if src[-1] != "/": # check whether the user input contain '/' at the end or not
        src = src + "/"
    dst = re.sub(r"\\", "/", dst) + "/"
    if dst[-1] != "/":
        dst = dst + "/"
    # print(src+"\n"+dst)

    if(os.path.exists(src) and os.path.exists(dst)): # check if the path exists
        files: list[str] = os.listdir(src) # create files list of folder
    else:
        return # stop the execution

    folders: list[str] = create_folders(src, files)

    move_files(src, dst, files)

def create_folders(dst: str, files: list[str])->list[str]:
    files_types = [] # list to mantain the record of the file types
    folders = [] # list to maintain the record of the folders for files
    
    for file in files:
        if "." in file: # check whether it is a file or a folder
            _ , fileType = file.split(".") # give the file name and its type
            type = f".{fileType}" 
            folderName = f"{fileType} files"# folder for the file type

            if type not in files_types:
                files_types.append(type)
            if folderName not in folders:
                folders.append(folderName)
    # print(files_types)
    # print(folders)
    for folder in folders:
        if not os.path.exists(dst + folder):
            os.makedirs(dst + folder)
    
    return folders
    
def move_files(src: str, dst: str, files: list[str])->None:
    for file in files:
        if "." in file:
            _, fileType = file.split(".")

            if not os.path.exists(dst + fileType + " files/"+file):
                shutil.move(src+file, dst+fileType+" files/"+file)
    
if __name__ == "__main__":
    main()
