#!/bin/bash
set -e
set -o pipefail
set -u
set -x

if [[ $# -ne 1 ]]; then
	echo "Must supply one argument"
	exit
fi

unzip ~/Downloads/$( ls -rt ~/Downloads/| tail -1 )
a=$1
n=${a%.py}

for i in in out ; do
    mv ${i}put001.txt ../${n}.${i}
    echo '' >> ../${n}.${i}
done
