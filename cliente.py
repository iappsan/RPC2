import xmlrpc.client

def main():
    proxy = xmlrpc.client.ServerProxy("http://172.16.8.23:5432")

    usr = ''
    clientState = 1
    clientPath = ''
    clientRootPath = ''
    # 1 - Autenticar cliente
    # 2 - Conexion remota
    # 3 - Salir

    while not clientState == 3:
        while clientState == 1:
            usr = input('Ingresa tu usuario:')
            psswd = input('Ingresa tu contrasena:')
            if (proxy.auth(usr, psswd)):
                clientRootPath = usr+'/'
                clientPath = clientRootPath
                print (f'Usuario {usr} ingresado\n')
                clientState = 2
            else:
                print ('Usuario o contrasena incorrectos\n')
        
        while clientState == 2:
            remoteOption = 0
            print (f'\nHola {usr}, que opcion quieres?\n')
            print ('1 .Renombrar archivo o carpeta')
            print ('2 .Borrar archivo')
            print ('3 .Crear carpeta')
            print ('4 .Borrar carpeta')
            print ('5 .Listar directorio')
            print ('6 .Cambiar de directorio')
            print ('7 .Modificar archivo')
            print ('8 .Crear archivo')
            print ('9 .PWD')
            print ('10 .Salir')
            remoteOption = int(input())

            if remoteOption == 1:
                print ('\n---------------------\n')
                print ('1 .Renombrar')
                oFile = clientPath + input('Nombre actual del archivo: ')
                nFile = clientPath + input('Nuevo nombre: ')
                print (proxy.rename(oFile, nFile))

            elif remoteOption == 2:
                print ('\n---------------------\n')
                print ('2 .Borrar archivo')
                fileName = clientPath + input('Archivo a borrar: ')
                print (proxy.remove(fileName))

            elif remoteOption == 3:
                print ('\n---------------------\n')
                print ('3 .Crear carpeta')
                fileName = clientPath + input('Nombre de la carpeta: ')
                print (proxy.mkdir(fileName))

            elif remoteOption == 4:
                print ('\n---------------------\n')
                print ('4 .Borrar carpeta')
                fileName = clientPath + input('Nombre de la carpeta: ')
                print (proxy.rmdir(fileName))

            elif remoteOption == 5:
                print ('\n---------------------\n')
                print (f'5 .Listar directorio\n\t{clientPath}')
                print (proxy.ls(clientPath))

            elif remoteOption == 6:
                print ('\n---------------------\n')
                print ('6 .Cambiar de directorio')
                newDir = input('A que carpeta? \n(Home - Para ir a tu raiz)\n')
                if newDir == 'Home':
                    clientPath = clientRootPath
                    print(f'Nuevo direcrotio: {clientPath}')
                else:
                    if proxy.cd(clientPath + newDir):
                        clientPath = clientRootPath+newDir+'/'
                        print(f'Nuevo direcrotio: {clientPath}')
                    else:                
                        print (f'Carpeta {newDir} no encontrada')

            elif remoteOption == 7:
                print ('\n---------------------\n')
                print ('7 .Modificar archivo')
                fileName = clientPath + input('Nombre del archivo: ')
                modStatus = 0
                # 0 - Edita
                # 1 - Salir
                while modStatus == 0:
                    print ('Archivo actual:\n')
                    fileLines = proxy.read(fileName)
                    for line in fileLines:
                        print(line)

                    rorw = input('Escribe lo que quieras agregar:\n(exit() para salir)\n')
                    if rorw == 'exit()':
                        modStatus = 1
                    else:
                        proxy.write(fileName, rorw)
                        print ('\n\n')
    
            elif remoteOption == 8:
                print ('\n---------------------\n')
                print ('8 .Crear archivo')
                fileName = clientPath + input('Nombre del archivo: ')
                print (proxy.createFile(fileName))

            elif remoteOption == 9:
                print ('\n---------------------\n')
                print ('9 .PWD')
                print (f'Directorio actual: {clientPath}')

            elif remoteOption == 10:
                print ('Saliendo ...')
                clientState = 3

            else:
                print('Opcion no valida')
                

if __name__ == '__main__':
    main()