#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


#/*
# * ----------------------------------------------------------------------------
# * "THE BEER-WARE LICENSE" (Revision 42):
# * <flipchan@riseup.net> wrote this file. As long as you retain this notice you
# * can do whatever you want with this stuff. If we meet some day, and you think
# * this stuff is worth it, you can buy me a beer in return Filip Kälebo
# * ----------------------------------------------------------------------------
# */


#hacked the SEC-T 2016 badge to a "usb key"
import os, gnupg, zipfile

#http://www.saltycrane.com/blog/2011/10/python-gnupg-gpg-example/
#gpg https://pythonhosted.org/python-gnupg/
gpg = gnupg.GPG(homedir='/media/NONAME/crypto')
gpg.encoding = 'utf-8'


def zipd(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


#zip, shred n remove, encrypt
def encrypt(to):
    to = str(to)
    zipf = zipfile.ZipFile('/media/NONAME/crypto/just_cute_cats.zip', 'w', zipfile.ZIP_DEFLATED)
    zipd('/media/NONAME/crypto/secret/', zipf)
    os.system('cd /media/NONAME/crypto/secret/ && shred * && cd /media/NONAME/crypto/secret/ && rm *')
    with open('just_cute_cats.zip', 'rb') as f:
        gpg.encrypt(f, to, output='file.txt.gpg')
        os.system('cd /media/NONAME/crypto/ && shred just_cute_cats.zip && cd /media/NONAME/crypto/ && rm just_cute_cats.zip')
        print 'ok'
        
def decrypt(password):
    password = str(password)
    with open('/media/NONAME/crypto/file.txt.gpg', 'rb') as f: #open/read file
        gpg.decrypt(f, passphrase=password, output='just_cute_cats.zip')
   
    print 'ok'


#no need 4 main dr jones
 
##if __name__ == '__main__':
##    zipf = zipfile.ZipFile('/media/NONAME/crypto/just_cute_cats.zip', 'w', zipfile.ZIP_DEFLATED)
    #zipd('/media/NONAME/crypto/secret/', zipf)
    ##shred n remove
    #os.system('cd /media/NONAME/crypto/secret/ && shred test.txt && cd /media/NONAME/crypto/secret/ && rm test.txt')
    #print 'ziped'
    #zipf.close()
    ##crypt the file
    #with open('just_cute_cats.zip', 'rb') as f:
        #gpg.encrypt_file(f, recipients=['root@localhost'], output='file.txt.gpg')
        #print 'encrypted'
        #os.system('cd /media/NONAME/crypto/ && shred just_cute_cats.zip && cd /media/NONAME/crypto/ && rm just_cute_cats.zip')
        #print 'done'
