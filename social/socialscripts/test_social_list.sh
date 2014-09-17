#!/bin/bash

TIMEFILE=social.list.time
ERRFILE=social.list.err
echo 'Starting run' >> $TIMEFILE
echo 'Starting run' >> $ERRFILE
date >> $TIMEFILE
date >> $ERRFILE

for iteration in 1 2 3 4 5 6 7 8 9 10
do 
  for ipaddress_port in $*
  do
    { time curl -o junk.file -s -S --max-time 5 http://$ipaddress_port/data/files.html 2>> $ERRFILE; } 2>> $TIMEFILE
  done
done

