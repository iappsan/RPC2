import os
print('\n')
uFile = open('users', 'r').readlines()
uList = []
uListF = []
for u in uFile:
    uList.append(u.replace('\n',''))
for user in uList:
    uListF.append(user.split('|'))

print (uListF[1][0])


os.chdir('321saas')