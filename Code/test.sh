#!/bin/sh
for f in *.py
do
	/usr/bin/time -f "%E" python "$f" | tail -1
done