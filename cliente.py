import xmlrpc.client

def main(args):
    proxy = xmlrpc.client.ServerProxy("http://localhost:5432")
    n1= input()
    n2= input()
    print ("Hola")
    print (proxy.test(n1,n2))

if __name__ == '__main__':
    main()