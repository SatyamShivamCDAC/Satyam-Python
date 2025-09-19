class FileManager:
    def __init__(self):
        print("file management system created")

    def create_file(self,str):
        file = str + ".txt"

        try:
            file1 = open(file, "w")
        except:
            print("Couldn't create a file")
        finally:
            file1.close()

    def write_file(self,str,message):
        file = str + ".txt"
        try:
            file1 = open(file,"w")
            file1.write(message + "\n")
            print("file written successfully")
        except:
            print("Couldn't write file")
        finally:
            file1.close()

    def read_file(self,str):
        file = str + ".txt"
        try:
            file1 = open(file,"r")
            data = file1.read()
            file1.seek(0)
            print(data)
            file1.close
        except:
            print("couldn't read file")

    def copy_file(self,str1,str2):
        str1 = str1 + ".txt"
        str2 = str2 + ".txt"
        try:
            file1 = open(str1,"r")
            data = file1.read()
            file2 = open(str2,"w")
            file2.write(data)
            file2.close()
            print("File copied successfully")
        except:
            print("Couldn't copy file")
        finally:
            file1.close()

filemanager = FileManager()

filemanager.create_file("file1.txt")
filemanager.create_file("file2")

filemanager.write_file("file1.txt","welcome to file1.txt")
filemanager.read_file("file1.txt")
filemanager.copy_file("file1.txt","file2")
