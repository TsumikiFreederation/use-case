#!/bin/bash
FILETOPUT=testfile

TIMEFILE=social.put.time
ERRFILE=social.put.err
echo 'Starting run' >> $TIMEFILE
echo 'Starting run' >> $ERRFILE
date >> $TIMEFILE
date >> $ERRFILE

for iteration in 1 2 3 4 5 6 7 8 9 10
do 
  for ipaddress_port in $*
  do
#    { time curl http://$ipaddress_port/down/index.html?file=onekilo.txt >> social.out 2>> social.err } >> social.out 2>> social.err;
    { time curl -s -S --form "filename=$FILETOPUT" --form "file=@$FILETOPUT" --max-time 5 http://$ipaddress_port/upload/index.html 2>> $ERRFILE > /dev/null; } 2>> $TIMEFILE
  done
done
