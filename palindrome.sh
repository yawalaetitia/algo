#!/bin/bash
function pair_element(){
   nombre=""
   for i in $@
   do
    if(($i%2==0))
    then
      nombre+=$i
    fi
 done
 if(($nombre))
 then
    echo $nombre
 else
    echo "0"
 fi
}
pair_element 1 1 1

