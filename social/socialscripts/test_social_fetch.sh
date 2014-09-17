#!/bin/bash

FILETOFETCH=testfile

TIMEFILE=social.fetch.time
ERRFILE=social.fetch.err
echo 'Starting run' >> $ERRFILE
echo 'Starting run' >> $TIMEFILE
date >> $ERRFILE
date >> $TIMEFILE

for iteration in 1 2 3 4 5 6 7 8 9 10
do 
  for ipaddress_port in $*
  do
#    { time curl http://$ipaddress_port/down/index.html?file=onekilo.txt >> social.out 2>> social.err } >> social.out 2>> social.err;
    { time curl -o junk.file -s -S --max-time 5 http://$ipaddress_port/down/index.html?file=$FILETOFETCH 2>> $ERRFILE; } 2>> $TIMEFILE
  done
done

