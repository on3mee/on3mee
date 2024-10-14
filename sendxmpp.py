#!/usr/bin/python
# -*- coding: utf-8 -*-

################################################
#                                              #
# SEND MESSAGE TO XMPP SERVER MEMBER (EJABBER) #
#                                              #
################################################

import sys
import os
from getpass import getpass
from pyxmpp2.simple import send_message

# CREDENTIALS OF PYXMPP2 ACCOUNT

your_jid = "meshtastic@meshtastic.localdomain" #Client account
your_password = "2022user12022"  #Password of client account
#target_jid = "admin@meshtastic.localdomain"  #Target account who receive messages

#message = sys.argv[1]

    
#send_message(your_jid, your_password, target_jid, message)

target_jid = "user1@meshtastic.localdomain"
message = sys.argv[1]

send_message(your_jid, your_password, target_jid, message)
time.sleep(10)
os.system("pyhon3 /home/admin/meshtalk/meshwatch.py")
