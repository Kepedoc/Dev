#!/bin/bash 

BACKUPTINE=`date +%b-%d-%y`

DESTENATION=/home/keped/backupfolder/ backup-$BACKUPTIME.tar.gz

SOURCEFOLDER=/home/keped/Backup_sorcefolder

tar -cpzf $DESTENATION $SOURCEFOLDER

crontab -e


