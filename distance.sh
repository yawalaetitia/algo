
#!/bin/bash
function palindrome(){
reverse=""

len=${#1}
for (( i=$len-1; i>=0; i-- ))
do 
	reverse="$reverse${1:$i:1}"
done
if [ $1 == $reverse ]
then
    echo "$1 is palindrome"
else
    echo "$1 is not palindrome"
fi
}
palindrome yawa