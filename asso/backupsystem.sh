#!/bin/bash

FULLDATE=$(date +%c)

FILENAME="/home/keped/backup/backup_sorcefolder/file"

BACKED=$(date +%N -r /home/keped/backup/backupfolder) 

SORCE=$(date +%N -r /home/keped/backup/backup_sorcefolder)

INITIALSIZE=$(cat $FILENAME | wc -c)

ARCHIVEDFILESIZE=$(tar ztvf $FILENAME -v --wildcards)

if [ $BACKED -gt $SORCE ]; 
then	

tar -cvf /home/keped/backup/backupfolder/kompressed /home/keped/backup/backup_sorcefolder

echo -e "most recent archivisation of $FILENAME at: $FULLDATE \n filesize cut down from $INITIALSIZE bites to $ARCHIVEDFILESIZE bites" >> /var/log/backup.log

else
echo "nothing is to be done"

fi

