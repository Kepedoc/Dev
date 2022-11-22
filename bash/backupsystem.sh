#!/bin/bash

LOG_LOC="/var/log/backup.log"

function check_dir_loc {
		if [ ! -s "/backup_dirs.conf" ]
		then
				echo "missing config! no information on where to look for backups"
				echo "create a backup_dir.conf in root directory"
				exit 1
		fi
}				
function check_backup_loc {
		if [ ! -s "/backup_loc.conf" ]
		then
				echo "missing config! no information on where to save the files"
				echo "create a backup_loc.conf in root directory"
				exit 1
		fi
}
function check_schedule {
		if [ ! -s "/etc/cron.weekly/make_backup" ]
		then
				sudo cp make_backup.sh /etc/cron.weekly/make_backup
				echo "Weekly backups will be made"
				echo "The exact time is in the /etc/crontab file"
				exit 1
		fi
}
function execute_backup {
		
		backup_path=$(cat /backup_loc.conf)

		echo "Starting backup..." > $LOG_LOC
		while read dir_path
		do 
			dir_name=$(basename $dir_path)
			filename=$backup_path$dir_name.tar.gz
			tar -zcf $filename $dir_path 2>> $LOG_LOC
			chown keped:keped $filename
			echo "backing up of $dir_name completed." >> $LOG_LOC
		done < /backup_dirs.conf

		echo "Backup finished at:" >> $LOG_LOC
		date >> $LOG_LOC
}

check_dir_loc
check_backup_loc
check_schedule
performe backup
