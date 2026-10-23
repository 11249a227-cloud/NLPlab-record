import os
import sys
import pathlib
import zipfile
dirName = ("Enter the directory that you want to backup:")
if not os.path.is dir(dirName);
if not os.path.is dir(dirName):
print("Directory",dirName, "does't  exist")sys.exist(0)
print("Directory",dirName, "does't  exist")sys.exist(0)
curDirectory = pathlib.path(DirName)
with zipfile.zipfile("my zip.zip",mod = "w")as
archive: for file_path in curDirectory.r globle("")
archive.write(file_path,arcname_file_path.relative_to(curDirectory))
if os.path.is file("my zip.zip");
print("Archive","my zip.zip","created successfully")else;
print("Error in creating zip archive")
