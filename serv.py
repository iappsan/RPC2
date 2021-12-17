from xmlrpc.server import SimpleXMLRPCServer
import os

userList = []

def verifyUserFile(usr):
    try:
        os.chdir(usr)
        os.chdir('..')

    except:
        os.mkdir(usr)

def auth(usr, password):
    global userList
    credOk = False
    for user in userList:
        if user[0] == usr:
            if user[1] == password:
                credOk = True

    if credOk:
        verifyUserFile(usr)
        return (f'Usuario {usr} accediendo {str(pwd())}')
    else:
        return (f'Usuario o contrasena incorrectos')

def createFile(newName):
    os.system(f'touch {newName}')

def rename(oldFile, newFile):
    str = ''
    try:
        os.rename(oldFile, newFile)
        str = f'archivo {oldFile} renombrado'
    except:
        str = 'No se pudo renombrar'
    return str

def remove(fileToRm):   #Borrar archivo
    str = ''
    try:
        os.remove(fileToRm)
        str = f'archivo {fileToRm} removido'
    except:
        str = 'No existe el archivo {fileToRm}'
    return str

def mkdir(folderName):  #Crear directorio
    str = ''
    try:
        os.mkdir(folderName)
        str = f'folder {folderName} creado'
    except:
        str = f'Ya existe {folderName}'
    return str

def rmdir(folderName):  #Borrar directorio
    str = ''
    try:
        os.rmdir(folderName)
        str = f'archivo {folderName} removido'
    except:
        str = f'No existe el folder {folderName}'
    return str

def ls():               #Listar
    output = os.popen('ls').read()
    return (output)

def cd(cdDir):          #Cambiar directorio
    os.chdir(cdDir)
    output = os.popen('pwd').read()
    str = f'Nueva dir: {output}'
    return str

def pwd():              #Imprime directorio
    output = os.popen('pwd').read()
    return output

def test():             #funcion de prueba
    print('\n')
    stream = os.popen('pwd')
    output = stream.read()
    return (output)

def rnw(fileName, text):
    str = ''
    try:
        myFile = open(fileName, 'r')
        lines = myFile.readlines()

    except:
        str = 'Error durante uso de archivo'
    return str


def main():
    global userList
    print ("Iniciando servidor ...")
    server = SimpleXMLRPCServer(("172.16.8.23", 5432))
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

    uFile = open('users', 'r').readlines()
    uList = []
    for u in uFile:
        uList.append(u.replace('\n',''))
    for user in uList:
        userList.append(user.split('|'))
    
    os.chdir('./Users/')

    print ("Servidor listo")
    server.serve_forever()

if __name__ == '__main__':
    main()