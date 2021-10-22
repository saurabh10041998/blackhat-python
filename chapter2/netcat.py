#! /usr/bin/python

import socket
import sys
import getopt
import threading
import subprocess

## -l, -e, -c, -u

# define some global variables
listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = "" 
port = 0

def usage():
    print "====== [*] BHP netcat tool ======"
    print
    print "usage: ./netcat.py -t target_host -p target_port options"
    print
    print "-l   --listen                    Listen on the port number\n \
                                for incomming connection"
    print "-e   --execute=file_to_execute   Upon  connection file to be\n \
                                executed on the target"
    print "-c   --command                   Initialize command shell"
    print "-u   --upload=destination        Upload a file to [destination]"
    print
    print "Examples: "
    print "./netcat.py -t 192.168.0.1 -p 5555 -l -c"
    print "./netcat.py -t 192.168.0.1 -p 5555 -e=\"cat /etc/passwd\""
    print "./netcat.py -t 192.168.0.1 -p 5555 -u=c:\\target.exe"
    print "echo ABCDEFGH | ./netcat.py -t 192.168.0.1 -p 5555"
    sys.exit(0)


def main():
    global listen
    global command
    global upload
    global execute
    global target
    global upload_destination
    global port

    if not len(sys.argv[1:]):
        usage()
    try:
        # parse the command line arguments
        options, _args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:", ["help", "listen", "execute=", "target=", "port=", "command", "upload="])
        # TODO: -upload not showing the invalid options error, plz check 
        for o, a in options:
            if o in ('--help', '-h'):
                usage()
            elif o in ('--execute', '-e'):
                execute = a
            elif o in ('--listen', '-l'):
                listen = True
            elif o in ('--command', '-c'):
                command = True
            elif o in ('--upload', '-u'):
                upload_destination = a
            elif o in ("--target", "-t"):
                target = a
            elif o in ("--port", "-p"):
                port = int(a)
            else:
                assert False, "Invalid option"
   
        # if we are not listening and just want to send data
        if not listen and len(target) and port > 0:
            # Read the input from stdin
            buffer = sys.stdin.read()

            # send the data
            if len(buffer):
                client_sender(buffer)
        # if we are going to listen and do C2
        # i.e upload, execute, drop a shell
        if listen:
            server_loop()

    except getopt.GetoptError as err:
        print str(err)
        usage()

def client_sender(buffer):
    None
def server_loop():
    None
main()
