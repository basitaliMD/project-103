import os
import shutil

from_dir = "C:/Users/Home/Downloads/python/Project-102"
to_dir = "C:/Users/Home/Desktop/Document_Files"
list_of_files = os.listdir(from_dir)

print(list_of_files)

for i in list_of_files:
    name, extension = os.path.splitext(i)
    if(extension == ''):
        continue
    if(extension in ['.pdf', '.doc', '.docx', '.txt']):
        path1 = from_dir + '/' + i
        path2 = to_dir + '/' + "Document_files"
        path3 = to_dir + '/' + "Document_files" + '/' + i
        if(os.path.exists(path2)):
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            shutil.move(path1, path3)