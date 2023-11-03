#!/bin/bash
echo "entrer un nombre"
read nbr
for ((i=1; i<=$nbr; i++))
do
  echo "-------"
  echo "TABLE de $i"
   for j in {1..10}
   do
      echo "$i*$j= $(($i*$j))"
   done
done
 

