#/bin/bash

FULLDATE=$(date +%c)

FILENAME=$(/home/keped/backup/backup_sorcefolder/experimentalfile)

A=$(date +%N -r /home/keped/backup/backupfolder) 

L=$(date +%N -r /home/keped/backup/backup_sorcefolder)

INITIALSIZE=$(wc -c /home/keped/backup/backup_sorcefolder/experimentalfile | awk '{print $1}')

ARCHIVEDFILESIZE=$(tar ztvf $FILENAME.tar.gz -v --wildcards '*FOOBAR*')

if [ $L -gt $A ]; 
then	

tar -czvf /home/keped/backup/backupfolder/$FILENAME.tar.gz /home/keped/backup/backup_sorcefolder

echo -e "most recent archivisation of $FILENAME at: $FULLDATE \n filesize cut down from $INITIALFILESIZE bites to > $ARCHIVEDFILESIZE bites" >> /var/log/backup.log

else

echo "nothing is to be done"

fi

