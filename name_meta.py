import os
from datetime import datetime
import piexif

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
            year=int(year)
            exif_dict = piexif.load(os.path.join(file_path, file_name))
            exif_dict['Exif'] = {
                piexif.ExifIFD.DateTimeOriginal: datetime(year, 1, 1, 12, 0, 0).strftime("%Y:%m:%d %H:%M:%S")}
            exif_bytes = piexif.dump(exif_dict)
            piexif.insert(exif_bytes, os.path.join(file_path, file_name))
            # print("FILE:", file_name, "YEAR:", year)
        else:
            print("FILE:", file_name, "YEAR: No year")
        year=""


if __name__ == '__main__':
    print("Run:", datetime.now())
    file_path = input("Desired file path")
    file_list = get_files(path=file_path)
    get_year(files=file_list)