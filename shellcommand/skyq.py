#!/usr/bin/env python
import sys
import socket
import math
import array
from time import sleep
host_ip = "192.168.0.15" #Sky Q box address
port = 5900

def sendcommand(host,command):
   code = getcode(command)
   cmd1 = int(math.floor(224 + (code/16)))
   cmd2 = int(code % 16)
   command1 = array.array('B', [4, 1, 0, 0, 0, 0, cmd1, cmd2]).tostring()
   command2 = array.array('B', [4, 0, 0, 0, 0, 0, cmd1, cmd2]).tostring()

   s = socket.socket()
   s.connect((host,port))  #connect to SkyQ box
   reply = s.recv(12)      #receive handshake
   s.send(reply)           #send handshake
   reply = s.recv(2)       #receive 2 bytes
   s.send(reply[0])        #send 1 byte
   reply = s.recv(4)       #receive 4 bytes
   s.send(reply[0])        #send 1 byte
   reply = s.recv(24)      #receive 24 bytes

   s.send(command1)        #send command bytes part 1
   s.send(command2)        #send command bytes part 2

   s.close()               #close connection

def getcode(cmdname):
   commands = {
      "power": 0,
      "select": 1,
      "backup": 2,
      "dismiss": 2,
      "channelup": 6,
      "channeldown": 7,
      "interactive": 8,
      "sidebar": 8,
      "help": 9,
      "services": 10,
      "search": 10,
      "tvguide": 11,
      "home": 11,
      "i": 14,
      "text": 15,
      "up": 16,
      "down": 17,
      "left": 18,
      "right": 19,
      "red": 32,
      "green": 33,
      "yellow": 34,
      "blue": 35,
      "0": 48,
      "1": 49,
      "2": 50,
      "3": 51,
      "4": 52,
      "5": 53,
      "6": 54,
      "7": 55,
      "8": 56,
      "9": 57,
      "play": 64,
      "pause": 65,
      "stop": 66,
      "record": 67,
      "fastforward": 69,
      "rewind": 71,
      "boxoffice": 240,
      "sky": 241
   }
   return commands[cmdname]

def getchannelno( channel ):
  chno = {
    'sky_news': 501,
    'sky_sports_main_event': 401,
    'sky_sports_action': 407,
    'sky_sports_arena': 408,
    'sky_sports_cricket': 404,
    'sky_sports_golf': 405
  }
  return chno[channel]

if len(sys.argv) == 1:
  print "no parameters"
  sys.exit(2)

if sys.argv[1] == "channel":
  if len(sys.argv) < 3:
    print 'USAGE:',sys.argv[0],'[<command>|channel <channel name>]'
    sys.exit(2)

  chno = getchannelno(sys.argv[2])

  sendcommand(host_ip,str(chno/100))
  sleep(0.2)
  sendcommand(host_ip,str((chno%100)/10))
  sleep(0.2)
  sendcommand(host_ip,str(chno%10))
elif sys.argv[1] == "chno":
  chno = int(sys.argv[2])

  sendcommand(host_ip,str(chno/100))
  sleep(0.2)
  sendcommand(host_ip,str((chno%100)/10))
  sleep(0.2)
  sendcommand(host_ip,str(chno%10))
else:
  sendcommand(host_ip,sys.argv[1])
