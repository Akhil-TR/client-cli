import sys
import os
import math
from flask import *
app= Flask(__name__)
#covert bytes into appropriate formate
def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("Byte", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])
#find size of the file
def fileSize(root,fileName):
    fSize=os.path.getsize(os.path.join(root, fileName))
    return(convert_size(fSize))
#list details of file
def list_files(path):
    width=20
    count=0
    data={}
    print("files in the Directory: "+path)
    print("{}|{}| {}| {}| {}".format("#".ljust(3),"File_name".ljust(10),"File_path".ljust(width),"File_size".ljust(width),"File_extension".ljust(width)))
    print("-----------------------------------------------------------------------------------------------------------")
    for root, dirs, files in os.walk(path):
        for file in files:
            g=file.split(".")
            e="."+g[-1]
            p=os.path.join(root,file)
            s=fileSize(root,file)
            count+=1
            # print("#"+str(count))
            # print("File_name:"+file)
            # print("File_Path:"+p)
            # print("File_size:"+s)
            # print("Extension:"+e)
            print("{}|{}| {}| {}| {}".format(str(count).ljust(5),file.ljust(20),p.ljust(width),s.ljust(width),e.ljust(width)))
            data[file]=[p,s,e]
   
def options():
    msg="Command Line Interfce for Traversing file system"
    print("****************************************************")
    print(msg)
    print("----------------------------------------------------")
    print("client <path> ===> To show files and its properties" )
    print("****************************************************")
#main code
def main():
    try:
    	qry=[]
    	for i in sys.argv:
        	qry.append(i)
    	if qry[-1]=="--help":
        	options()
    	else:
        	data=list_files(qry[-1])
        	print(data)
    except:
    	print("Directory not found")
    app.run(debug=True)

@app.route('/',methods=['POST'])
def getInfo():
    return jsonify(data)
if __name__ == '__main__':
    main()
