#if else
import getpass

username = 'hale'
password = '123'
passinggrade = 75

u = input ("Enter username :")
p = getpass.getpass ("Enter password :")

if username == u and password == p:
   print ('Access Granted')
   
   

   
else: 
   print('Access denied')