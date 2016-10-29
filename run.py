from CrYpt0r import decrypt, encrypt #our file
import getpass

print ''' 
			sec-t badge hack
 _______  _______  ___________         _______ 
|       || 2016  ||           |       |       |
|  _____||    ___||           | ____  |_     _|
| |_____ |   |___ |           ||____|   |   |  
|_____  ||    ___||      _____|         |   |  
 _____| ||   |___ |     |_____          |   |  
|_______||_______||b_a_d_g_e__|         |___|  

	A pgp/gpg wannabe yubikey
	     made by ~flipchan
'''


print 'enter 1 or 2'
what = raw_input('Decrypt[1] or encrypt[2]?:')

if what=='1':
	print 'Decryption'
	passwd = getpass.getpass('Enter Password: ')
	decrypt(passwd)
	print 'files decrypted!'
	
elif what=='2':
	print 'Encryption'
	to = raw_input('Enter email address of recipient: ')
	encrypt(to)
	print 'files encrypted!'

else:
	print 'error'
