#!/bin/bash

#######################################################
#                                                     #
#  SCRIPT TO START MESHTASTIC - XMPP EJABBER GATEWAY  #
#                                                     #
#######################################################

# When flag = 1, meshwatch.py run well
# When flag = 0, meshwatch.py are crashed, this script will restart 
# meshwatch.py as a watchdog
# You can put this script in /etc/init.d to start on boot


rm -f flag.txt
echo "1" >> flag.txt

python3 meshwatch.py

p=1
while p=1 
do
  sleep 1
  while IFS= read -r line; do flag=$line; done < flag.txt
  echo $flag
  if ( flag=0 )
  then
     python3 /home/admin/meshtalk/meshwatch.py
     rm -f flag.txt
     echo "1" >> flag.txt
  fi
done

     
