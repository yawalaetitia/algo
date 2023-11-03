#!/bin/bash
<< # echo "entrer un mot:"
read word
reverse=""
len=${#1}
for ((i=$len-1; i>=0; i--))
do
    reverse=$reverse${1:$i:1}
done
if(($reverse==$1))
then
    echo "palindrome"
else
  echo "non palindrom"
fi >>