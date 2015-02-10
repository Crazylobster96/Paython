#!/usr/bin/python
# UDP Broadcast Server
import socket, traceback, sys
import threading, time

lglock = threading.Lock()
msglock = threading.Lock()
logcount = 0
LogMessage = []
MessageBox = []


def write_erro(errstr):
    global lglock, msglock,logcount, LogMessage, MessageBox
    logtime=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    log = logtime+' Error:  '+log
    lglock.acquire()
    LogMessage.append(log)
    logcount += 1
    f_log = open('log.txt','a')
    while (logcount > 0):
            f_log.write(LogMessage[0])
            f_log.write('\n')
            LogMessage.remove(LogMessage[0])
            logcount -= 1
        f_log.close()
    lglock.release()
    
def write_log(log):
    global lglock, msglock,logcount, LogMessage, MessageBox
    logtime=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    log = logtime+' Log:  '+log
    lglock.acquire()
    LogMessage.append(log)
    logcount += 1
    if(logcount == 4096):
        f_log = open('log.txt','a')
        while (logcount > 0):
            f_log.write(LogMessage[0])
            f_log.write('\n')
            LogMessage.remove(LogMessage[0])
            logcount -= 1
        f_log.close()
    lglock.release()
    
def Sync_log():
    global lglock, msglock,logcount, LogMessage, MessageBox
    lglock.acquire()
    if(logcount > 0):
        f_log = open('log.txt','a')
        while (logcount > 0):
            f_log.write(LogMessage[0])
            f_log.write('\n')
            LogMessage.remove(LogMessage[0])
            logcount -= 1
        f_log.close()
    lglock.release()

def BroadCast(b_message,timeout):
    dest = ('<broadcast>',port)
    broadcast_s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    broadcast_s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
    broadcast_s.sendto(b_message,dest)

def BrdC_Recv():
    host = ''
    port = 51423
    RecS = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    RecS.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    RecS.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
    RecS.bind((host,port))
    while 1:
        try:
            message,address = s.recvfrom(8192)
            print "Got data from",address
    
def Main_thread():
    global lglock, msglock,logcount, LogMessage, MessageBox
    write_log('Main thread start!')
    #start recv thread;
    
    #broadcast self
    #join thread recv;
    Sync_log()
     
def main():
    Main_thread()

if __name__ == '__main__':
    main()
    

    

