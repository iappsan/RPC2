from xmlrpc.server import SimpleXMLRPCServer
import os

userList = []

def verifyUserFile(usr):    # Verifica la carpeta del usuario
    try:
        os.chdir(usr)
        os.chdir('..')

    except:
        os.mkdir(usr)

def auth(usr, password):    # Autenticar usuario
    global userList
    credOk = False
    for user in userList:
        if user[0] == usr:
            if user[1] == password:
                credOk = True

    if credOk:
        verifyUserFile(usr)
        return (True)
    else:
        return (False)

def createFile(newName):    # Crea un archivo
    os.system(f'touch {newName}')

def rename(oFile, nFile):   # Renombrar 1
    str = ''
    try:
        os.rename(oFile, nFile)
        str = f'archivo {oFile} renombrado'
    except:
        str = 'No se pudo renombrar'
    return str

def remove(fileToRm):   #Borrar archivo 2
    str = ''
    try:
        os.remove(fileToRm)
        str = f'archivo {fileToRm} removido'
    except:
        str = 'No existe el archivo {fileToRm}'
    return str

def mkdir(folderName):  #Crear directorio 3
    str = ''
    try:
        os.mkdir(folderName)
        str = f'folder {folderName} creado'
    except:
        str = f'Ya existe {folderName}'
    return str

def rmdir(folderName):  #Borrar directorio 4
    str = ''
    try:
        os.rmdir(folderName)
        str = f'archivo {folderName} removido'
    except:
        str = f'No existe el folder {folderName}'
    return str

def ls(homeDir):               #Listar 5
    output = os.popen(f'ls {homeDir}').read()
    return (output)

def cd(cdDir):          #Cambiar directorio 6
    try:
        os.chdir(cdDir)
        os.chdir('..')
        return True
    except:
        return False

def pwd():              #Imprime directorio
    output = os.popen('pwd').read()
    return output

def read(fileName):    # Modifica archivo 7
    str = ''
    try:
        str = open(fileName, 'r').readlines()
    except:
        str = 'Error durante lectura de archivo'
    return str

def write(fileName, text):
    str = ''
    try:
        myFile = open(fileName, 'a')
        myFile.write(text)
        myFile.close()
    except:
        str = 'Error durante escritura de archivo'
    return str

def main():
    global userList
    print ("Iniciando servidor ...")
    server = SimpleXMLRPCServer(("172.16.8.23", 5432))
    server.register_function(auth)
    server.register_function(createFile)
    server.register_function(read)
    server.register_function(write)
    server.register_function(rename)
    server.register_function(remove)
    server.register_function(mkdir)
    server.register_function(rmdir)
    server.register_function(ls)
    server.register_function(cd)

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