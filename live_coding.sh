#!/bin/bash
function somme(){
    res=0
    for ((i=0; i<=1000; i++))
    do
      res=$(($res+$i))
    done
    echo $res    
}
somme