#!/bin/bash
read -p "Enter many values:" data
array=($data)
size=${#array[@]}
for ((i=0;i<$size;i++))
do
   for((j=0;j<$size-1;j++))
   do
     if ((${array[$j]}<${array[$j+1]}))
     then
         temp=${array[$j+1]}
         array[$j+1]=${array[$j]}
         array[$j]=$temp
     fi
    done
done
echo ${array[@]}         