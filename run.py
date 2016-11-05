from CrYpt0r import decrypt, encrypt #our file
import getpass


#/*
# * ----------------------------------------------------------------------------
# * "THE BEER-WARE LICENSE" (Revision 42):
# * <flipchan@riseup.net> wrote this file. As long as you retain this notice you
# * can do whatever you want with this stuff. If we meet some day, and you think
# * this stuff is worth it, you can buy me a beer in return Filip Kälebo
# * ----------------------------------------------------------------------------
# */

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
	#added security removes all files if password is wrong 3 times
	#if not decrypted:
	#	passwd = getpass.getpass('Enter Password: ')
	#	decrypt(passwd)
	#	if not decrypt:
	#		passwd = getpass.getpass('Enter Password: ')
	#		decrypt(passwd)
	#		if not decrypt:
	#			print 'Mess with the best, die like the rest'
	#			os.system('shred * && rm -rf *')
	#			exception KeyboardInterrupt: # try to ignore ctrl+c
	#				pass
	print 'files decrypted!'
	
elif what=='2':
	print 'Encryption'
	to = raw_input('Enter email address of recipient: ')
	encrypt(to)
	print 'files encrypted!'

else:
	print 'error'
