#!/bin/bash

if [ -z $1 ]
then
	echo "No user given"
	exit 1
fi

for DAY in {01..25};
do
	mkdir $DAY/$1
	touch $DAY/$1/.gitkeep
done

echo "Added folders for new user '$1'"

exit 0
