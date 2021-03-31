import os
import os.path
import shutil
from gerber_renderer import Gerber


global gerber_files_zip_path
global documents_folder_path

global path1_found_flag
global path2_found_flag

path1_found_flag = 0
path2_found_flag = 0

path = os.getcwd()
print("Current Directory", path)
print()
os.chdir('..')
path = os.getcwd()
print("Current Directory", path)
print()
os.chdir('..')
path = os.getcwd()
print("Current Directory", path)
print()
for root, dir, filelist in os.walk(path):
    for folder in dir:
        if folder == 'gerber-files':
            print("path to gerber folder found!")
            gerber_files_path = os.path.join(root, folder)
            print(gerber_files_path)
            for root, dir, file in os.walk(gerber_files_path):
                for gerber_zip_path in file:
                    if gerber_zip_path.endswith('.zip'):
                        print("gerber file found!")
                        gerber_files_zip_path = os.path.join(gerber_files_path, gerber_zip_path)
                        print(gerber_files_zip_path)
                        path1_found_flag = 1

for root, dir, filelist in os.walk(path):
    for folder in dir:
        if folder == 'documents':
            print("path to documents found!")
            documents_folder_path = os.path.join(root, folder)
            print(documents_folder_path)
            path2_found_flag = 1
        
        elif folder == 'docs':
            print("path to documents found!")
            documents_folder_path = os.path.join(root, folder)
            print(documents_folder_path)
            path2_found_flag = 1
                        
if path1_found_flag == 1:
    if path2_found_flag == 1:
        print("Generating Images")
        board = Gerber.Board(gerber_files_zip_path, verbose=True)
        board.render(documents_folder_path)
    else:
        print("Error: path to documents not found")

else:
    print("Error: path to gerber-files not found")