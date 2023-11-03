#!/bin/bash
echo "entrer un nombre compris entre 10 et 20 :"
read nbr
while [[ $nbr -lt 10  ]] || [[ $nbr -gt 20 ]]
do 
  if [[ $nbr -gt 20 ]]
  then 
     echo "<< Plus petit!>>" 
  elif [[ $nbr -lt 10 ]]
  then
     echo "<< Plus grand!>>"
  fi
 echo " entrer un nombre compris entre 10 et 20 :"
 read nbr

done

