#!/bin/bash

DATE=$(date +%m:%d:%y)

tar -czvf /home/keped/backup/backupfolder/$DATE.tar.gz /home/keped/backup/backup_sorcefolder

echo  "second backup" > /var/log/backup.log

