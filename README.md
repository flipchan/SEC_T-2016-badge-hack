# SEC_T-2016-badge-hack
hacked the sec-t 2016 badge to a wannabe yubi key

encrypts a folder in on the badge with pgp/gpg

tested on kali linux 1-2 and debian 7

you need to install python-gnupg, tested with python2.7
```console
/media/NONAME# ls
Carl Svensson   Francisco Blas Izquierdo Riera  Löwinder      Ulf Frisk
Coresec         Joahim.Fredrik.Peter            Mattias Borg  Vesa Virta
crypto          Knowit                          Sentor        
Försvarsmakten  Love Björk                      Tyler Bohan



ls crypto/
CrYpt0r.py    just_cute_cats.zip  pubring.gpg   run.py       
trustdb.gpg   pubring.gpg~  secret
file.txt.gpg  random_seed   secring.gpg
```

i have created a dir on the badge called crypto and generated gpg keys in that dir 
gpg --gen-key --home-dir=/media/NONAME/crypto

then i create a folder called secret where i put all the stuff i want to encrypted

so the keys are on the badge

then just run it:
```console
python run.py
root@computer:/media/NONAME/crypto# python run.py 
 
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

enter 1 or 2
Decrypt[1] or encrypt[2]?:2
Encryption
Enter email address of recipient: root@localhost
ok
files encrypted!
```
