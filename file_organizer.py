import os, shutil, re

def main()->None:

    src: str = input("Enter the source file path: ")
    dst: str = input("Enter the destination file path: ")
    
    src = re.sub(r"\\", "/", src)
    if src[-1] != "/":
        src = src + "/"
    dst = re.sub(r"\\", "/", dst) + "/"
    if dst[-1] != "/":
        dst = dst + "/"
    # print(src+"\n"+dst)

    if(os.path.exists(src) and os.path.exists(dst)):
        files: list[str] = os.listdir(src)
    else:
        return 

    folders: list[str] = create_folders(src, files)

    move_files(src, dst, files)

def create_folders(dst: str, files: list[str])->list[str]:
    files_types = []
    folders = []
    
    for file in files:
        if "." in file:
            _ , fileType = file.split(".")
            type = f".{fileType}"
            folderName = f"{fileType} files"

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