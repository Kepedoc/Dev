#! bin/bash

while true; do
	xsetroot -name "$(acpi -b | awk '{print $4}') | $(date '+%R %a %d.%m')"
	sleep 1m
done
