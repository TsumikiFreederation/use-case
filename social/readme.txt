To run this social storage code, unpack the attached tarball, copy in a keypair (to be used for encryption and decryption), and then do:

python repy.py RESTRICTIONSFILE dylink.r2py librepy.r2py blockstore.py KEYFILENAME PORTNUM

For example: 
python repy.py restrictions.full dylink.r2py librepy.r2py blockstore.py justinc 12345

Then we can point a web browser at the system (IP:port) and see the interface.  To upload files, use: upload/index.html  To download files, use: down/index.html  To list the set of stored files, use: data/files.html There are also other options like stopping the server remotely, etc. you can find off the main page.

For evaluation convenience, there is a set of scripts that time different operations.  These scripts require that 'curl' is installed on the local system to operate.  Simply call a script with one or more hostname:port entries to perform testing.  It will make the requested call 10 times on each system and log the timing information.

The scripts are:
test_social_fetch.sh
test_social_list.sh
test_social_put.sh

An example set of calls is:
./test_social_list.sh 192.168.1.114:12345
./test_social_list.sh 192.168.1.114:12345
./test_social_put.sh 192.168.1.114:12345
./test_social_fetch.sh 192.168.1.114:12345

Their output goes into files: 
social.fetch.err	
social.fetch.time
social.list.err
social.list.time
social.put.err
social.put.time
