import os
from datetime import datetime

def get_files(path):
    files = os.listdir(path)
    return files

def get_year(files):
    year=""
    for file_name in files:
        for char in file_name:
            # print(char, ":", char.isdigit())

            if char.isdigit():
                if len(year)!=4:
                    if char.isdigit():
                        year=year+char
            else:
                if len(year)<4:
                    year=""
        if year[0:2]=="19" or year[0:2]=="20":
            print("FILE:", file_name, "YEAR:", year)
        else:
            print("FILE:", file_name, "YEAR: No year")
        year=""


if __name__ == '__main__':
    print("Run:", datetime.now())
    file_list = get_files(path="test_pictures")
    get_year(files=file_list)