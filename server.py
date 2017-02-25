import os
import web
import json
import threading
import pickle
import io
import glob

'''
#Requests==2.13.0
#Read port selected by the cloud for our application
PORT = int(os.getenv('PORT', 8000))
# Change current directory to avoid exposure of control files
os.chdir('static')

httpd = Server(("", PORT), Handler)
try:
  print("Start serving at port %i" % PORT)
  httpd.serve_forever()
except KeyboardInterrupt:
  pass
#httpd.server_close()

os.chdir('.')
'''

str="ds"
print(str)
print("rest service")

urls = ('/(.*)', 'API')
app = web.application(urls, globals())

PORT = int(os.getenv('PORT', 8000))

db = []


# Very simple REST API application built with web.py
class API():
    def GET(self, id=None):
        global db
        x=id.split("/")
        for file in glob.glob("*.txt"):
            db.append(file)
        print(db)
        option=x[0]
        if(option=="3"):
            id=x[1]
            id=id+".txt"
            lines=[]
            if(id in db):
                with open(id) as f:
                    for line in f:
                        line = line.strip('\n')
                        line=line.encode('utf-8')
                        lines.append(line)
                print(lines)
                return json.dumps(lines)
            else:
                return web.notfound()
        elif(option=="4"):
            filename=x[1]
            filename=filename+".txt"
            book=x[2]
            if(filename in db):
                with open(filename) as f:
                    for line in f:
                        line = line.strip('\n')
                        line=line.encode('utf-8')
                        line=line.split(" ")
                       
                        if(line[0]==book):
                            return json.dumps(line[1])

            return web.notfound()


    def POST(self, id=None):
        global db
        #x=json.loads(web.data())
        print(id)
        value=id.split("/")
        print("value : ",value[0])
        if(value[0]=="1"):
            filename=value[1]+".txt"
            db.append(filename)
            print(filename)
            f= open(filename,"w+")
            f.close()
        elif(value[0]=="2"):
            detailsofbook=[value[2],value[3],value[4],value[5]]
            category=value[1]
            category=category+".txt"
            with open(category, 'a+') as f:
                for s in detailsofbook:
                     #f.write((s + " ").encode('unicode-escape'))
                     f.write(s + " ")
                f.write("\n")
       
        return json.dumps('created')

    def DELETE(self, id):
        global db
        for file in glob.glob("*.txt"):
            db.append(file)
        
        x=id.split("/")
        option=x[0]
        if(option=="5"):
            filename=x[1]
            filename=filename+".txt"
            book=x[2]
            output=[]
            if(filename in db):
                print("hi")
                with open(filename) as f:
                    for line in f:
                        line = line.strip('\n')
                        line=line.encode('utf-8')
                        linebook=line.split(" ")
                        print(linebook)
                        line=" ".join(x for x in linebook)
                        if(linebook[0]!=book):
                            output.append(line)
                print("output : " ,output)
                f = open(filename, 'w')
                f.truncate()
                for ele in output:
                    f.write(ele+'\n')
                f.close()
                return json.dumps("Book deleted")          

            return json.dumps("category or book not present")

        elif(option=="6"):
            filename=x[1]
            filename=filename+".txt"
            if(filename in db):
                os.remove(filename)
                return json.dumps("deleted")          

            return json.dumps("file does not exist") 
           

    def PUT(self, id):
        global db
        for file in glob.glob("*.txt"):
            db.append(file)
        
        x=id.split("/")
        option=x[0]

        if(option=="7"):
            filename=x[1]
            filename=filename+".txt"
            book=x[2]
            newcost=x[3]
            output=[]
            print("book is "+ book+"\n")
            if(filename in db):
                with open(filename) as f:
                    for line in f:
                        line = line.strip('\n')
                        line=line.encode('utf-8')
                        linebook=line.split(" ")
                        line=" ".join(x for x in linebook)
                        if(linebook[0]!=book):
                            output.append(line)
                        else:
                            linebook[1]=newcost
                            line=" ".join(x for x in linebook)
                            output.append(line)

                #print("output is : ",output)
                f = open(filename, 'w')
                f.truncate()
                for ele in output:
                    f.write(ele+'\n')
                f.close()
                return json.dumps("updated")
            else:
                return json.dumps("file does not exist")
           

def run_server():
    thread = threading.Thread(target = app.run)
    thread.start()
    return thread

if(__name__ == "__main__"):
    app.run();

