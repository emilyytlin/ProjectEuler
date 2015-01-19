#!/bin/sh
TIMEFORMAT=%R
max=60

function ok() {
    awk -v n1=$1 -v n2=$2 'BEGIN{ if (n1>=n2) exit 0; exit 1}'
}

for f in *.py
do
	echo python "$f"
	out=$( { time python "$f"; } 2>&1 )
	if [ $? -ne 0 ]; then
		echo "error"
		exit $?
	fi
	arr=($out)
	ans=${arr[0]}
	elapsed=${arr[${#arr[@]}-1]}
	echo "$elapsed"
	ok $max $elapsed
	if [ $? -ne 0 ]; then
		echo "time limit exceeded"
		exit $?
	fi
	echo "-------------------"
done