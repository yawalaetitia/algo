#!/bin/bash
read -p "Entrer des valeurs:" data
array=($data)
min=0
for i in ${array[@]}
do
  if (($min>$i))çu_
  then
      min=$i
  fi
done  
echo $min