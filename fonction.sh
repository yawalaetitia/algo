#!/bin/bash
read -p "entrer un nombre : " nbr
resultat=1
for (( i=1;i<=$nbr;i++ ))
do
 resultat=$(($resultat*$i))
done
echo $resultat

  