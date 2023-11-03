#!/bin/bash
read -p "entrer un nombre:" p
if(($p%2==0))
then
   echo "$p is even"

else 
echo "$p is not even"
fi
 