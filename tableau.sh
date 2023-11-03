#!/bin/bash
 function est_palindrome(){
    reverse=""
    len=${#1}
    for ((i=$len-1; i>=0; i--))
    do
       reverse="reverse${$1:$i:1}"
    done
    if (($1==$reverse))
    then
         echo "vrai"
    else 
        echo "faux"
   fi
 }
 est_palindrome yawa
