import csv
from sys import platform
import os
def update_csv_file():
    path = ''
    if platform == 'linux':
            path = 'files/'
    elif platform == 'win32':
            path = 'files\\'
    dir_list = os.listdir(path)

    with open('dir.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['name','modifiedDate','createdDate','size','type'])
        data = []
        for i in dir_list:
            fn, file_ext = os.path.splitext(path+i)
            fn += file_ext
            print('------------------------')
            print("File name: {}\nModified date: {}\nCreated date: {}\nSize: {}\nType: {}".format(i,os.path.getmtime(fn),os.path.getctime(fn),os.path.getsize(fn),file_ext))
            data.append([i,os.path.getmtime(fn),os.path.getctime(fn),os.path.getsize(fn),file_ext])
        print('------------------------\n')    
        writer.writerows(data)

    with open("dir.csv", newline='') as f:
        reader = csv.reader(f)
        fileNames = []
        for row in reader:
            fileNames.append(row[0].lower())
            print(row)
        return fileNames[1:]
