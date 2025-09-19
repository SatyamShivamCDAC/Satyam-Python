from IPython.core.splitinput import line_split


class FileOps:
    def __init__(self):
        print("Welcome to file ops")

    @staticmethod
    def vowel_count(str1):
        file = str1 + ".txt"
        vowels = ['a','e','i','o','u']
        try:
            file1 = open(file,"r")
            data =  file1.read()
            vowel_count = 0
            for ch in data:
                if ch.lower() in vowels:
                    vowel_count += 1
            file1.seek(0)
            file1.close()
            return vowel_count
        except:
            print("couldn't find file")

    @staticmethod
    def word_count(str1):
        count = 0
        file = str1 +".txt"
        try:
            file1 = open(file,"r")
            data = file1.read()
            for ch in data:
                if ch.isalnum():
                    count += 1
            file1.close()
            file2 = open("word_count.txt","w")
            file2.write("Number of words in " + str1 + " is " + str(count))
            file2.close()
        except:
            print("couldn't open file")

    @staticmethod
    def remove_blank(stt):
        file = stt + ".txt"
        info = []
        try:
            file1 = open(file,"r")
            data = file1.read()
            for ch in data:
                if ch.isalnum():
                    info.append(ch)
            info_str = ''.join(info)
            file1.close()

            file2 = open("removed_spaces.txt","w")
            file2.write(info_str)
            file2.close()
        except:
            print("Couldn't copy file with removing blanks")

    @staticmethod
    def merge_files(str1,str2):
        str1 = str1 + ".txt"
        str2 = str2 + ".txt"
        try:
            file1 = open(str1, "r")
            file2 = open(str2, "r")
            data1 = file1.read()
            data2 = file2.read()
            data = data1 + "\n" + data2
            file1.close()
            file2.close()

            file3 = open("merged_file.txt","w")
            file3.write(data)
            file3.close()
            print("merged file successfully")

        except:
            print("Couldn't merge file")

    @staticmethod
    def encrypt_file(fstr):
        file = fstr + ".txt"
        cipher_key = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v',
                      'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e',
                      's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm', 'A': 'N',
                      'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S', 'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W',
                      'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A', 'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F',
                      'T': 'G', 'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}

        try:
            file1 = open(file,"r")
            data = file1.read()
            code = []
            for ch in data:
                if ch.isalnum():
                    code.append(cipher_key[ch])
                else:
                    code.append(ch)
            encryted = ''.join(code)
            file1.close()
            file2 = open("encryted_code.txt","w")
            file2.write(encryted)
            file2.close()
        except:
            print("Couldn't encryt code")

    @staticmethod
    def decrypt_file():

        cipher_key = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v',
                      'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e',
                      's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm', 'A': 'N',
                      'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S', 'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W',
                      'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A', 'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F',
                      'T': 'G', 'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}

        try:
            file1 = open("encryted_code.txt","r")
            data = file1.read()
            code = []
            for ch in data:
                if ch.isalnum():
                    code.append(cipher_key[ch])
                else:
                    code.append(ch)
            decryted = ''.join(code)
            file1.close()
            file2 = open("decryted_code.txt","w")
            file2.write(decryted)
            file2.close()
        except:
            print("Couldn't decryt code")

    @staticmethod
    def replaceDataInFile(fstr,str1,str2):
        file = fstr + ".txt"
        data_arr = []
        with open(file,"r") as file1:
            data = file1.read()
            data_arr = data.split('\n')
            for line in data_arr:
                line_split = line.split()
                for word in line_split:
                    if word == str1:
                        line_split[line_split.index(word)] = str2
                sentence = "".join(line_split)



FileOps.replaceDataInFile("file1","is","IS")

