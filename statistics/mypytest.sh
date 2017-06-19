#!/bin/bash

set -e
set -u
set -o pipefail

a=${1##*/}
n=${a%.py}

#
# check syntax with pep8
#
echo -ne "pep8:\t"
set +e
pep8 $n.py
RC=$?
set -e
if [[ $RC -eq 0 ]] ; then
	echo PASS
else
	echo FAIL
	exit 1
fi

#
# check if executable bit set
#
[[ -x $n.py ]] || chmod u+x $n.py

#
# check input/output
#
echo -ne "output:\t"
f=$(mktemp)
./$n.py < $n.in > $f

set +e
diff $f $n.out
RC=$?
set -e
if [[ $RC -eq 0 ]] ; then
	echo PASS
else
	echo FAIL
	cat $f
fi

rm -f $f
