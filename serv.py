from xmlrpc.server import SimpleXMLRPCServer

def auth(user, password):
    pass

def createFile(newName):
    pass

def rnw(fileName, text):
    pass

def rename(oldFile, newFile):
    pass

def remove(fileToRm):
    pass

def mkdir(folderName):
    pass

def rmdir(folderName):
    pass

def ls():
    pass

def cd(cdDir):
    pass

def test(a, b):
    return a+b


def main():
    print ("Iniciando servidor ...")
    server = SimpleXMLRPCServer(("localhost", 5432))
    server.register_function(auth)
    server.register_function(createFile)
    server.register_function(rnw)
    server.register_function(rename)
    server.register_function(remove)
    server.register_function(mkdir)
    server.register_function(rmdir)
    server.register_function(ls)
    server.register_function(cd)
    server.register_function(test)
    print ("Servidor listo")
    server.serve_forever()

if __name__ == '__main__':
    main()