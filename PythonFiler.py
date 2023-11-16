#imports
import os
import shutil


#path to downloads C:\Users\dange\Downloads
path = 'C:\Users\dange\Downloads'

list_ = os.listdir(path) #list of files in downloads

for file_ in list:
    name, ext = os.path.splitext(file_)
    ext = ext[1:]
    if ext == '':
        continue
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)
