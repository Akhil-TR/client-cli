import sys
import os
import math
def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("Byte", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])
def fileSize(root,fileName):
	fSize=os.path.getsize(os.path.join(root, fileName))
	return(convert_size(fSize))
def list_files(path):
    count=0
    print("File_name\t\tFile_path\t\tFile_size\t\tFile_extension")
    print("--------------------------------------------------------")
    for root, dirs, files in os.walk(path):
    	for file in files:
			g=file.split(".")
			print(file+"\t\t"+os.path.join(root, file)+"\t\t"+fileSize(root,file)+"\t\t"+"."+g[-1])
			

    print(count)
def main():
    args = sys.argv[1:]
    for arg in args:
    	p=format(arg)
    print(p)
    list_files(p)
if __name__ == '__main__':
    main()