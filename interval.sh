#!/bin/bash
function fact(){
res=1
for((i=1; i<=$1; i++))
do
   res=$(($res * $i))
done
echo $res
}
fact 4