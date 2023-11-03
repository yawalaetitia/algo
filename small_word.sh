#!/bin/bash
function small_word(){
array=($1)
mot=${array[0]}

for i in ${array[@]}
do
    if((${#i}<${#mot}))
    then
        mot=$i
    fi
done
echo $mot 
}    
small_word  "maman est belle"      