for i in {1..255}; do awk '$5{if ('$i'==$5) {print $1, $5, $6 > $5}}' server.log; done

for file in [0-9]*; do mv $file $file.logsep; done

# to do all files:

for file in *.logsep;
do 
  awk '{if (prev == 0) {print "Starting at", $1; strt = $1} else if ($1 - prev < 290) {print "suspiciously short time!!!", $1-prev, $1, prev} else if ($1 - prev > 900) {print "ended at",prev, "alive for",prev-strt;strt = $1; print "resumed at",$1,"gap of",$1-prev;}prev = $1; } END {print "Finished at",prev, "alive for",prev-strt}' $file | grep alive  | awk '$NF>0{print $NF/3600}';
done
