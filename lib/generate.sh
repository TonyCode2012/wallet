#!/bin/bash
resFile="foundPrime.log"
generatePy="genBigPrime.py"
TMPFILE=".TMPFILE"
bigPrime=""

true > $TMPFILE

python $generatePy
if [ ! -s $TMPFILE ]; then
    echo "[ERROR] find big prime failed!" >&2
    exit 1
else
    bigPrime=`cat $TMPFILE`
fi

if ! cat $resFile | grep "$bigPrime" &>/dev/null; then
    echo "$bigPrime" >> $resFile
else
    echo "[WARNING] Having found $bigPrime before!"
fi
