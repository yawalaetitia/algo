#!/bin/bash
function est(){
reverse=""

len=${#1}
for (( i=$len-1; i>=0; i-- ))
do 
	reverse="$reverse${1:$i:1}"
done
if [$input -eq $reverse]
then
    echo "$input is palindrome"
else
    echo "$input is not palindrome"
fi
}
est "awa"