#!/bin/bash
echo "Entrer un nombre"
read nbr
if [[ $nbr -gt 16 ]] && [[ $nbr -lt 20 ]]
then
    echo "très bien"
elif [[ $nbr -gt 14 ]] && [[ $nbr -le 16 ]]
then 
    echo "bien"
elif [[ $nbr -gt 12 ]] &&  [[ $nbr -le 14 ]]
then 
    echo "assez bien"
elif [[ $nbr -gt 10 ]] && [[ $nbr -le 12 ]] 
then
    echo "moyen"
else
   echo "insuffisant"
fi
  
