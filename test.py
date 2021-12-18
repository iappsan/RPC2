import os
print('\n')
uFile = open('users', 'r').readlines()
uList = []
uListF = []
for u in uFile:
    uList.append(u.replace('\n',''))
for user in uList:
    uListF.append(user.split('|'))

print (uListF)

myFile = open('users', 'a')
str1 = 'cosaoc|3222\n'
myFile.write(str1)
myFile.close()
