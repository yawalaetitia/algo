#!/bin/bash
function nombre_premier(){

    for((i=2; i<=$(($1/2)); i++))
    do
       if(($1%$i==0))
       then
           echo "non"
           break
        fi
    done
     echo "oui"     
}
nombre_premier 9