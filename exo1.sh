#!/bin/bash
read -p "entrer un nombre:" nbr
for ((i=1; i<=10; i++))
do
   res=$((nbr+i))
   echo -n $res " "
done
