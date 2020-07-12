#!/usr/bin/env sh

for t in "__pycache__" "*.pyc"; 
do 
    for f in `find ./ -name $t`; 
    do 
        rm -rf $f; 
    done; 
done;