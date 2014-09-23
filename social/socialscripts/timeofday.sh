sed -i".bak" '9,415d' server.log

awk '{if (prev == 0) {strt = $1; startline = NR} else if($1-strt>=7200) {strt = $1; startline = NR; for (i in node) n++; print $1, n; delete node; n=0} else if ($5) {node[$5]++} prev = $1; }' server.log > online.txt

